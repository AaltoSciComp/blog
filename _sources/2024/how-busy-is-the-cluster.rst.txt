:blogpost: true
:date: 2024-10-21
:author: Richard Darst
:category: triton


How busy is the cluster?  A discussion
======================================

We occasionally get some questions: how busy is the cluster?  How
long do I have to wait?  Is there some dashboard that can tell me?

The answer is, unfortunately, not so easy.  :external:doc:`Our cluster
<triton/index>` uses dynamic scheduling with a fairshare algorithm.
All users have a fairshare priority, which decreases the more you have
recently run.  Jobs are ranked by priority (including fairshare plus
other factors), and scheduled in that order.  If there are
unschedulable holes between those jobs, it can take a job with a lower
priority and fill them in ("backfilling").  So that gives us:

- A small-enough job with a low priority might still be scheduled
  soon.
- A higher priority user could submit something while you are waiting,
  and increase your wait time.
- An existing job could end early, making other wait times shorter.
- An existing job could end early, allowing some other higher priority
  jobs to run sooner, making backfilled jobs run later.

In short: there is no way to give an estimate of the wait time, in the
way people want.  We've tried but haven't find a way to answer the
question well.

What can we know?


Priority comparison
-------------------

You can compare your fairshare factor with other users.  If you run
``sshare`` you can see the fairshare (higher means higher priority).
``sprio`` shows relatively priority for all jobs (here, the raw values
are multiplied by some factor and added).  On Triton (the new install
since 2024 may), they mean the following:

* The "age" value is "1e4 × (1-(time_in_queue/7day))" (but maxes out
   at 7 days) (zero when first submitted, increasing to 10000 at 7
   days old)
* The fairshare factor is "1e7 × FairShare priority from sshare"

  * The FairShare value is computed based on the raw usage value: at
    each level of the share tree, it divides it up among the users so
    that those who have run less have a higher priority.

  * The usage value decays with a two-week half life.

* The others are mostly constant.

Still: this is all very abstract and what others submit has more
effect than your priority.  The only thing you can control is using
less resources.

This is quite cluster dependent so we'd recommend asking for help for
how your own cluster is setup.


How to get jobs scheduled sooner
--------------------------------

This may be your real question. There are two main things:

* Use less resources.  **Make sure you don't over-request more than
  you need (CPU, memory, GPUs)** - this will affect your future
  fairshare less. Of course, use everything you need, "saving for
  later" doesn't give you more resources than you save now.

* Request less resources per job.  This will let you be backfilled
  into the scheduling holes (see below).


When the cluster is mostly empty
--------------------------------

In this case, if there is a slot for you, you are scheduled very soon.
``srun --test [RESOURCE_REQUESTS]`` might give you some hint about
when a job would be scheduled - it basically tries to schedule an
empty job and reports the currently estimated start time. (It uses a
JobID though so don't run it in a loop)


The cluster has a long queue
----------------------------

In this case, nothing can be said since the queue is always being
re-shuffled.  In the long-run, you get a fair share of resources.  If
you haven't used much lately, you have more now.  Your wait time
depends more on what other users submit (and their priorities) than
what you submit - and this is always changing.  You can tell something
about how soon you'd be scheduled by looking at your priority relative
to other users.  Make your jobs as small and efficient as possible to
fit in between the holes of other jobs and get scheduled as soon as
possible.  If you can break one big job into smaller pieces (less
time, less CPU, less memory) that depend on each other, then you can
better fit in between all of the big jobs.  See the `Tetris metaphor
here in TTT4HPC
<https://coderefinery.github.io/TTT4HPC_resource_management/scheduling/>`__

If your need is "run stuff quickly for testing", make sure the jobs
are as short as possible.  Hopefully, your cluster staff about
development or debugging partitions that may be of use, because that's
the solution for quick tests.


Long, older description
-----------------------

This description was in an old version of our docs but has since been
removed.  The exact values are out of date.  It's included here for
detailed reference anyway:


Triton queues are not first-in first-out, but "fairshare".  This means
that every person has a priority.  The more you run the lower your
user priority.  As time passes, your user priority increases again.
The longer a job waits in the queue, the higher its job priority goes.
So, in the long run (if everyone is submitting an never-ending stream
of jobs), everyone will get exactly their share.

Once there are priorities, then: jobs are scheduled in order of
priority, then any gaps are backfilled with any smaller jobs that can
fit in.  So small jobs usually get scheduled fast regardless.

*Warning: from this point on, we get more and more technical, if you
really want to know the details.  Summary at the end.*

What's a share?  Currently shares are based on department and their
respective funding of Triton (``sshare``).  It used to be that
departments had a share, and then each member had a share of that
department.  But for complex reasons we have changed it so that it's
flat: so that each person has a share, and the shares of everyone in a
department corresponds to that department's share.  When you are below
your share (relative to everyone else), you have higher priority, and
vice versa.

Your priority goes down via the "job billing": roughly time×power.
CPUs are billed at 1/s (but older, less powerful CPUs cost less!).
Memory costs .2/GB/s.  But: you only get billed for the max of memory
or CPU. So if you use one CPU and all the memory (so that no one else
can run on it), you get billed for all memory but no CPU.  Same for
all CPUs and little memory.  This encourages balanced use.  (this also
applies to GPUs).

GPUs also have a billing weight, currently tens of times higher than a
CPU billing weight for the newest GPUs.  (In general all of these can
change, for the latest info see search ``BillingWeights`` in
``/etc/slurm/slurm.conf``).

If you submit a long job but it ends early, you are only billed for
the actual time you use (but the longer job might take longer to start
at the beginning).  Memory is always billed for the full reservation
even if you use less, since it isn't shared.

The "user priority" is actually just a record how much you have
consumed lately (the billing numbers above).  This number goes down
with a half-life decay of 2 weeks.  Your personal priority your share
compared to that, so we get the effect described above: the more you
(or your department) runs lately, the lower your priority.

If you want your stuff to run faster, the best way is to more
accurately specify your time (may make that job can find a place
sooner) and memory (avoids needlessly wasting your priority).

While your job is pending in the queue SLURM checks those metrics
regularly and recalculates job priority constantly.  If you are
interested in details, take a look at `multifactor priority plugin
<https://slurm.schedmd.com/priority_multifactor.html>`__ page (general
info) and `depth-oblivious fair-share factor
<https://slurm.schedmd.com/priority_multifactor3.html>`__ for what we
use specifically (warning: very in depth page).  On Triton, you can
always see the latest billing weights in ``/etc/slurm/slurm.conf``

Numerically, job priorities range from 0 to 2^32-1.  Higher is
sooner to run, but really the number doesn't mean much itself.

These commands can show you information about your user and job
priorities:

.. csv-table::
   :delim: |

   ``slurm s``         | list of jobs per user with their current priorities
   ``slurm full``      | as above but almost all of the job parameters are listed
   ``slurm shares``    | displays usage (RawUsage) and current FairShare weights (FairShare, higher is better) values for all users
   ``sshare``          | Raw data of the above
   ``sprio``           | Raw priority of queued jobs
   ``slurm j <jobid>`` | shows ``<jobid>`` detailed info including priority, requested nodes etc.

..
   ``slurm p gpu``       |     # shows partition parameters incl. Priority=


Summary
-------

tl;dr: Just select the resources you think you need, and Slurm
tries to balance things out so everyone gets their share.  The best
way to maintain high priority is to use resources efficiently so you
don't need to over-request.
