:blogpost: true
:date: 2021-04-14
:author: Marijn van Vliet
:category: python


What code has to teach us #1: the impact of implicit behavior
=============================================================

    | "The master has failed more times than the beginner has even tried"
    | -- Stephen McCranie

As Research Software Engineers (RSEs), we read and write a lot of code.
In this series of blog posts, we are going to share some snippets that taught us important lessons, and thereby impart that wisdom unto you.
These snippets are taken from actual research code, responsible for producing results that end up in peer-reviewed scientific articles.
That is to say, results that we should have some confidence in to be correct.
However, problems have a way of cropping up in the most unexpected places and when they do, there is a chance to learn from them.


The impact of implicit behavior
-------------------------------

I was in the metro zooming through Lauttasaari when I received an email from my professor that made my heart skip a beat.
We just submitted a paper to Nature Communications and were all still a little giddy about finally sending off the project we had been working on for 3 years.
She and the first author had been chatting about the cool methods we had been using for the project and a question arose: were we 100% certain that we "removed copies of the selected stimuli from the train set"?
If we hadn't, we would have to quickly pull back our submission, but surely we had, right?
I thought we did.
At least, I distinctly remember writing the code to do it.
Just to be on the safe side, I decided to double check the code.

Below is the analysis script in question.
It reads some data, performs some preprocessing, feeds into the a machine learning algorithm called ``zero_shot_decoding``, and stores the output.
I present it here to you in full, because there are many subtleties working together that make this situation so scary.
The question I pose to you, dear reader, is this: were the highlighted lines (118--120) executed, or did we have to pull our submission?

.. code-block:: python
   :linenos:
   :emphasize-lines: 118,119,120

    import numpy as np
    from scipy.io import loadmat, savemat
    from scipy.stats import zscore
    from zero_shot_decoding import zero_shot_decoding
    #print('Code version:'+ subprocess.check_output(['git', 'rev-parse', 'HEAD']))

    # Default location of the norm data (see also the --norms command line parameter)
    norm_file = '../data/corpusvectors_ginter_lemma.mat'

    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Run zero-shot learning on a single subject.')
    parser.add_argument('input_file', type=str,
                        help='The file that contains the subject data; should be a .mat file.')
    parser.add_argument('-s', '--subject-id', metavar='Subject ID', type=str, required=True,
                        help='The subject-id (as string). This number is recorded in the output .mat file.')
    parser.add_argument('--norms', metavar='filename', type=str, default=norm_file,
                        help='The file that contains the norm data. Defaults to %s.' % norm_file)
    parser.add_argument('-o', '--output', metavar='filename', type=str, default='results.mat',
                        help='The file to write the results to; should end in .mat. Defaults to results.mat')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Whether to show a progress bar')
    parser.add_argument('-b', '--break-after', metavar='N', type=int, default=-1,
                        help='Break after N iterations (useful for testing)')
    parser.add_argument('-n', '--n_voxels', metavar='N voxels', type=int, default=500,
                        help='Number of voxels. Used only for results file name.')
    parser.add_argument('-d', '--distance-metric', type=str, default='cosine',
                        help=("The distance metric to use. Any distance implemented in SciPy's "
                              "spatial.distance module is supported. See the docstring of "
                              "scipy.spatial.distance.pdict for the exhaustive list of possitble "
                              "metrics. Here are some of the more useful ones: "
                              "'euclidean' - Euclidean distance "
                              "'sqeuclidean' - Squared euclidean distance "
                              "'correlation' - Pearson correlation "
                              "'cosine' - Cosine similarity (the default)"))
    args = parser.parse_args()

    verbose = args.verbose
    if args.break_after > 0:
        break_after = args.break_after
    else:
        break_after = None

    print('Subject:', args.subject_id)
    print('Input:', args.input_file)
    print('Output:', args.output)
    print('Norms:', args.norms)
    print('Distance metric:', args.distance_metric)


    m = loadmat(args.input_file)
    if 'brainVecsReps' in m:
        # File without stability selection enabled
        print('Stability selection DISABLED')
        X = np.array([m['brainVecsReps'][0][i] for i in range(m['brainVecsReps'][0].shape[0])])
        n_repetitions, n_stimuli, n_voxels = X.shape
        voxel_ids = []

        # Drop all voxels that contain NaN's for any items
        non_nan_mask = ~np.any(np.any(np.isnan(X), axis=1), axis=0)
        non_nan_indices = np.flatnonzero(non_nan_mask)
        X = X[:, :, non_nan_mask]

        # Normalize betas across items
        X = zscore(X, axis=1, ddof=1)

        # Average over the repetitions
        X = X.mean(axis=0)

        X_perm = None
        splits = None

    elif 'mask_voxels' in m:
        # File without stability selection enabled
        print('Stability selection DISABLED')
        X = m['mask_voxels']
        voxel_ids = m['voxel_ids']
        n_stimuli, n_voxels = X.shape
        X_perm = None
        splits = None
        
    elif 'top_voxels_perm' in m:
        # File with stability selection enabled
        print('Stability selection ENABLED')
        X_perm = m['top_voxels_perm']
        X = m['top_voxels_all']
        voxel_ids = m['top_voxel_ids']
        n_stimuli, n_voxels, _ = X_perm.shape

        assert os.path.isfile('leave2out_index.npy')
        splits = np.load('leave2out_index.npy')

    elif 'brainVecs' in m:
        # File with single-trial data
        print('Stability selection DISABLED, single-trial data')
        X = m['brainVecs']
        voxel_ids = m['voxindex']
        n_stimuli, n_voxels = X.shape
        X_perm = None

        def generate_splits(n_stimuli, block_size=60):
            """Generate train-set, test-set splits.

            To save computation time, we don't do the full 360*359/2 iterations.
            Instead we will do the leave-2-out scheme block-wise and use the rest
            of the data for training.
            """
            assert n_stimuli % block_size == 0
            n_blocks = n_stimuli // block_size
            for x in range(n_stimuli):
                for y in range(x + 1, n_stimuli):
                    # Don't make the model distinguish between duplicate stimuli
                    if x % block_size == y % block_size:
                        continue

                    test_set = [x, y]
                    train_set = np.setdiff1d(np.arange(n_stimuli), test_set)

                    # Remove copies of the selected stimuli from the train set
                    train_set = np.setdiff1d(train_set, [i * block_size + (x % block_size) for i in range(n_blocks)])
                    train_set = np.setdiff1d(train_set, [i * block_size + (y % block_size) for i in range(n_blocks)])

                    yield train_set, test_set

        splits = generate_splits(n_stimuli)

    else:
        raise RuntimeError('Could not find any suitable data in the supplied input file.')

    # Load the norm data
    m = loadmat(args.norms)
    y = m['newVectors']

    if not np.isfinite(y).all():
        raise RuntimeError('The norm data contains NaNs or Infs.')
    if not np.isfinite(X).all():
        raise RuntimeError('The brain data contains NaNs or Infs.')

    pairwise_accuracies, model, target_scores, predicted_y, patterns = zero_shot_decoding(
        X, y, X_perm, verbose=verbose, break_after=break_after, metric=args.distance_metric, cv_splits=splits
    )

    savemat(args.output, {
        'pairwise_accuracies': pairwise_accuracies,
        'weights': model.coef_,
        'feat_scores': target_scores,
        'subject': args.subject_id,
        'inputfile': args.input_file,
        'alphas': model.alpha_,
        'voxel_ids': voxel_ids,
        'predicted_y': predicted_y,
        'patterns': patterns,
    })


Lessons this code has to teach us
---------------------------------

The first thing that went through my head, as it probably went through yours, was: this code is so long and complicated, answering this seemingly simple question is going to take some time to figure out.
And I won't blame you for giving up right then and there.
Hunched over my laptop while the metro passed through Ruoholahti, I tried to trace the logic of the script.

First problem: much of the behavior of the script is dictated by the command line arguments.
Luckily, their values are saved in the output file, so I could check that they were correct.

.. note::
    **Lesson:** always error on the side of caution when deciding whether it is worth storing something in the result file.

That brings us to the big ``if``-statement.
Did the correct branch execute?
Well, that depends on what was in the ``m`` dictionary, which translates to what variables were defined in the MATLAB file used as input to the script.
If we had used the wrong variable name, i.e. ``brainVecsReps`` instead of ``brainVecs``, when creating the input file, the wrong branch would have executed and the script would have been happily computing the wrong thing.
And we would never know.
If we had used the wrong input file, or the wrong version of the input file, the wrong branch would have executed without any indication that something was wrong.
So many opportunities for small mistakes to lead to a big error.

.. note::
    **Lesson:** have the user be explicit in what they want to do, so the script can check the user's intent against the inputs and raise a nice big error if they screwed up.
    In this case, there should really have been either a command line parameter determining which branch to execute, or even better, this should have been four separate scripts.

In the end I ended up searching the logfile for the line ``Stability selection DISABLED, single-trial data`` which, thankfully, was there, so the correct branch did execute.

.. note::
    **Lesson:** be liberal with ``print``-statements (or other logging directives) in your scripts; cherish the resulting logfiles.

I breathed a sigh of relieved as the metro pulled into the central railway station.

This ``if``-statement is a work of insanity.
What was I thinking determining what the script should be doing based on a mostly random naming scheme of some variables in a MATLAB file?
I got lucky that time.
But from that moment on, I would heed this lesson:

.. note::
    | Explicit is better than implicit.
    | -- The Zen of Python, by Tim Peters
