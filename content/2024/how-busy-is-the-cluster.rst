:blogpost: true
:date: 2024-04-18
:author: Richard Darst
:category: triton


How busy is the cluster?  A discussion
======================================

We occasionally get some questions: how busy is the cluster?  How
long do I have to wait?  Is there some dashboard that can tell me?

The answer is, unfortunately, not so easy.  :external:doc:`Our cluster
<triton/index>` uses dynamic scheduling with a fairshare algorithm.
All users have a priority, and jobs are ranked by priority, and
scheduled in that order.  If there are unschedulable holes between
those jobs, it can take a job with a lower priority and fill them in.
Users priority decrease when they run more.  So that gives us:

- A small-enough job with a low priority might still be scheduled
  soon.
- A higher priority user could submit something while you are waiting,
  and increase your wait time.
- A existing job could end early, making all other wait times shorter.

In short: there is no way to give an estimate of the wait time, in the
way people want.  We've tried but haven't find a way to answer the
question well.

What can we know?



Priority comparison
-------------------

You can compare your priority with other users.  If you run ``sshare``
you can see the shares.

TODO: how to interpret sshare?

This is quite cluster dependent so we'd recommend asking for help for
how your own cluster is setup.


When the cluster is mostly empty
--------------------------------

In this case, if there is a slot for you, you are scheduled very soon.
``srun --test [RESOURCE_REQUESTS]`` might give you some hint about
when a job would be scheduled - it basically tries to schedule an
empty job


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
possible.  See the `Tetris metaphor here in TTT4HPC
<https://coderefinery.github.io/TTT4HPC_resource_management/scheduling/>`__

If your need is "run stuff quickly for testing", make sure the jobs
are as short as possible.  Ask your cluster staff about development or
debugging partitions that may be of use.
