:blogpost: true
:date: 2023-08-08
:author: Richard Darst, Mira Salmensaari
:category: software, AI, whisper


Whisper deployed on Triton, LLMs coming
=======================================

.. highlight:: console



Whisper now easily available for researchers
---------------------------------------------

.. seealso::

   `Whisper on Triton documentation
   <https://scicomp.aalto.fi/triton/apps/whisper/>`__

`OpenAI Whisper <https://github.com/openai/whisper>`__ is a tool for
speech transcription.  It works well and has potential applications
in many different research and non-research use cases.  Using it isn't
too hard - if you can install it and if you have a GPU.  Often, the
installing can become a big barrier, especially for "just testing".

Luckily, we have a `cluster <https://scicomp.aalto.fi/triton/>`__ with
GPUs and a way to provide software for researchers.  We've made
Whisper available on the cluster as a `module
<https://scicomp.aalto.fi/triton/tut/modules/>`__, so it's trivial to
use it for any audio data you may have.  All one needs to do is::

  $ module load whisper
  (help gets printed out)
  $ srun --mem=6G singularity_wrapper run YOUR_FILE.wav --model_directory $medium --local_files_only True --language en

It might look complicated, but all you need to do is copy and paste.
The first words request the resources, the middle specifies your file,
and the last are some standard options to make it do things like use
our pre-downloaded model files.  Yes - this still requires knowledge
of how to use a cluster in general, but once you've got that
knowledge, transcribing audio is trivial.  We have a `self-study
course <https://scicomp.aalto.fi/triton/#tutorials>`__ on cluster
usage, and users can always drop by and `ask us for help
<https://scicomp.aalto.fi/help/>`__, for example our daily garage each
day.

See the `Whisper on Triton documentation
<https://scicomp.aalto.fi/triton/apps/whisper/>`__ for more
information on the use.

We are also preparing a way to do this through the cluster web
interface `Open OnDemand
<https://scicomp.aalto.fi/triton/usage/ood/>`__, which will remove
most of the need to know how a cluster works and make the tool even
more accessible to other communities.



LLMs and other tools next
-------------------------

We hope to make other tools available like this.

Whisper is just one of the latest tools, but you've probably noticed
that large language models are very popular these days.  There are, in
fact, some that can run locally on our own cluster, and our goal is to
deploy more of these so that they can be easily tested and used.  The
intention isn't to make a replacement for existing LLM services, but
make internal for testing, research, and development use easier.

Local installs have various benefits, including lower cost (since we
already own the hardware), being able to ensure reproducibility
longer-term (since models are locally downloaded and preserved), and
being able to use without various registrations.  The downside is that
the most popular ones ones aren't available for local use.



The role of ASC
---------------

**Contact us if you need other models deployed, or if you have trouble
using what's already out there.  We are still in an early phase, and
there will probably be some difficulties in availability,
accessibility, and reusability.** `Contact us early if you notice
anything that's not right <https://scicomp.aalto.fi/help/>`__.  We
both help installing things and `help using them as a research
engineer partner <https://scicomp.aalto.fi/rse/>`__.

It's clear that artificial intelligence and machine learning tools
will become more critical tools for other research.  The difficulty in
deploying and using them could become a barrier, and that is where
Aalto Scientific Computing comes in.  It's our goal to make sure the
infrastructure that researchers need is ready and able to be used by
everyone, not just those with classic HPC experience.



Tech details: difficulties and solutions
----------------------------------------

*Here we go over some implementation details, which may help others
who want to deploy similar things on their own clusters.  If you just
want to use things, you don't need to read on.*

We installed whisper in a `container
<https://en.wikipedia.org/wiki/Singularity_(software)>`__, so that all
dependencies are packaged together and things are portable.  The model
definitions themselves are *not* included in the container, but
mounted in.  We try to find options that allow one to specify the
model and model directory, so that the user can try out different
models without downloading each one.  The Lmod module file prints out
some help when loaded.

We've got two versions installed: normal Whisper, and
Whisper-diarization (which can identify speakers in the transcript).

Whisper and diarization both have multiple different
implementations. It's bit of guesswork to try to see which one is the
easiest to get running / works the best (not about quality of
transcript, but easy of deployment in container and with local
models). This led to a change to another implementation of diarization
midway since the current one is more active in development and seems
overall slightly better. A lot of the work was fortunately
transferable to the new implementation.

There were the common issues with getting the right dependencies in a
container and getting the GPUs to work there.  This is pretty standard
by now.

Most implementations of whisper want to download models when running
it. This might make sense for general user, but doesn't really make
sense on cluster. Depending on the implementation, getting it to use
local models is not always trivial. Since GPU execution of diarization
uses several models at once, there doesn't seem to be a simple way to
have it use local models at all without changing the code. It also
required some sleuthing to find where exactly the models are
downloaded.  If a code uses Hugging Face, `these environment variables
<https://huggingface.co/docs/huggingface_hub/main/en/package_reference/environment_variables>`__
can be useful.

Making a module that is both easy/practical to use for users without
also losing options is usually bit tricky: we want users to be able to
do anything, for "the right thing" to happen automatically, and not
build some opaque framework to make it happen.  Singularity-wrapper
fortunately helps quite a bit in doing lot of background stuff such as
binding directories, gpu flags, etc. cleanly without users having to
care about it, while still giving the option to run the container
straight through Apptainer/Singularity if finer control is necessary.

Testing if the containers work is somewhat annoying. Diarization in
particular saves a lot of cache files all over the place, which all
need to be purged when testing GPU running. Otherwise the GPU will
stay idle since everything it would do is already in cache.  This also
affects clean-up after users run the code.

A minor inconvenience for us (but possibly large for users) is that
the syntax for each Whisper CLI implementation tends to differ
slightly. This makes swapping between implementations slightly
annoying since you have to check every time what was the syntax for
flags.
