:blogpost: true
:date: 2026-04-16
:author: Richard Darst
:category:


The dilemma of setting Slurm parameters
=======================================

Sometimes people come to us and complain that there are idle cluster
GPUs, and they could be used if there wasn't a per-user limit on max
GPUs that any one user could use at once.  Other people come to us and
complain that all GPUs are in use by various people, and they can't
start jobs quickly.

Perhaps you see the dilemma.  People both expect there are usually
available GPUs for them, and also that GPUs can be used to the fullest
extent.  We'll use GPUs as an example here, but this isn't specific to
GPUs.

We are very aware of this and try to enable as much overall research
as possible.  Still, there are choices to be made, and in this post we
will try to describe them, so that our users can better give feedback
for how we should adjust things.

We wrote this post so users can understand what's going on in the
background and let us know when something seems wrong.


Broad picture
-------------

A HPC cluster is fundamentally designed for batch work: for a given
amount of resources, schedule them as efficiently as possible to get
the maximum amount of computation out, with as high resource
utilization as possible.  We, and many clusters, have some resources
reserved for interactive use, since interactive testing and debugging
is extremely useful for getting work done.

We also have a "fairshare" system, where the use of users should be
equalized over the long run.  This means that if one user runs a lot
now (because the cluster was somewhat empty), their priority will be
less later.  The Triton priority decay half-life is 14 days.


Problem: one user is running too many jobs
------------------------------------------

The situation: one user is dominating GPU use.  Is this fair?

If one user was able to fill up the cluster, that means that at that
time the jobs started, there were no other users waiting for those
resources.  If there were multiple users waiting, then the resources
would have been split a bit more fairly (according to their
priorities).

Don't worry, once their current jobs finish, their priority will be
much lower and everyone else will have a much higher priority to run
next.


Problem: All GPUs are full until X days from now
-------------------------------------------------

Situation: one user has a lot of GPUs in use.  I know I can wait for
them to finish, but they last many days.  Do I really have to wait
X days before I can get stuff started?

Sometimes, if the cluster is free, a user can submit many long jobs.
This means resources aren't being wasted right now (which is good),
but the resources remain occupied for that duration (max time 3 or 5
days on Triton).  This is a bit annoying.  This is mainly a problem
when the cluster is mostly empty, since if there are lots of things
running, jobs turn over frequently enough that people can get some
resources quickly (and the heavy users have lower priority at the
time, so the more recent users have priority for free slots).

In this case, we usually wait and just let the situation develop, and
once we get
to a "steady state fullness" jobs cycle fast enough it's not usual for
the cluster to get to this state.  There aren't that many free GPUs
opening up all at once without multiple users queuing, so it can't get
overloaded by one user.

We don't want to prohibit all long jobs, since long jobs are useful
especially for new users.  Yes, heavy users can and should adapt to
checkpointing and mainly using small jobs, but we don't want to force
everyone to go straight into hardest, purest way of using a cluster.

One option is the Slurm partition parameter ``GrpTRESRunMins``
("Trackable RESources Run Minutes"): this is a limit not on number of
jobs, or length of jobs, but sum(job_resources×job_length).  If this
was 120 GPU-hours, then one could run one 5-day job, or thirty 4-hour
jobs at once.  By tuning this, we can make it where one can run long
jobs, or use all the cluster, but not use all the cluster with long
jobs.


Problem: the cluster has free slots but I'm not allowed to use them
-------------------------------------------------------------------

Situation: There are free GPUs, but Slurm doesn't let me use them.
Isn't this a waste?

Clearly this is the opposite situation of the two situations above.
We'd normally like to prevent this situation, but there are some
reasons it may occur.  Sometimes, we do have a limit on the max number
of jobs that can run.  Hopefully this is temporary while we work
something out.  Sometimes, we have various resources reserved for
short jobs, for interactive jobs, and so on.  Sometimes someone has
bought their own dedicated resources and we want to leave some
available for them.


Problem: I can't get work done in time for a deadline
-----------------------------------------------------

Situation: I have a conference deadline in a few days, and I need as
many resources as possible to finish my submission.

Unfortunately, this isn't really how a cluster works.  It could work
for clusters that are really bought by one group and they can decide
what runs, but Triton resources are bought for general use and we
don't free up resources for deadlines.  The fairshare system may also
affect you here, with you getting less resources if you have used a
lot in the past.

There are other clusters that may be usable and have more free
resources (or you may have higher priority since you haven't run as
much there lately).  It's good if you can make your code portable, or
ask for our help early enough in your work and we can help do that.


Problem: It takes too long to iterate code during development
-------------------------------------------------------------

Situation: Each time I submit a job, I have to wait to see if it
works, edit, and try again.  This is slow.

Indeed.  We try to save some resources in a debug partition
(``gpu-debug``), which are in theory always available (but have a very
short time limit, like 15 minutes).  However, it's only easy to
allocate a whole node to a debug partition, and four or more GPUs is a
lot to spend on a partition that's mostly idling, so sometimes we
don't have the most advanced GPUs available there.

Triton's GPU debug partition does overlap with a lot of different
other nodes and has a high partition priority, so if you submit there
it'll hopefully run ASAP.

We also have interactive partitions, which you can open in OnDemand to
do development work.  We don't have GPUs with huge memory there, since
interactive GPUs are mostly idle and not doing computing (we mainly
have older GPUs and Multi-instance-GPUs (MiGs) which split one GPU
into several with smaller memory).  Everything in the rest of this
post, about balancing amount used and convenience, can be repeated
with interactive GPUs.  The more we give for interactive work, the
more GPUs are idle overall.  It's a balance we are constantly trying
to adjust.


Problem: I see a user is using GPUs inefficiently
-------------------------------------------------

Situation: I've tried to see what is slowing stuff down, and noticed
one user has low GPU efficiency.  Should they really be using GPUs in
that case?

We aren't aiming for maximum GPU calculations, we aim for getting the
most work done.  Some work is CPU-bound but GPUs can speed up part of
it.  Some work uses other third-party code and can't be optimized.
Sometimes the bottleneck is just somewhere else but the GPU still
significantly speeds things up.  With this, we don't want to prevent
someone from doing their work just because it's not perfectly
GPU-bound.

We do scan for low efficiency users and invite them to garage to see
if we can make things faster.  If someone is using expensive
resources, we consider there's an obligation to work with us to make
the usage as efficient as possible.  And yes, sometimes they are using
the GPUs optimally for their own case.  Also note that GPU occupancy
doesn't mean the GPU is doing useful work - sometimes the measures can
be off.

If you see a user that you think is inefficiently using the resources,
don't contact them yourself (unless you are their friend, colleague,
etc.).  Let us know and we'll investigate if we haven't done so yet.


Problem: others are using my group's dedicated resources
--------------------------------------------------------

Situation: My group has purchases dedicated resources and they are
working as part of the cluster.  Someone else is using them, and it
slows down our use.

We set up the way resources are shared when someone gets the
resources.  Normally, the deal is we want overall highest use of the
cluster, since after all the university is also contributing
significant sysadmin and electricity resources.  We don't necessarily
guarantee that you can use it right away, but we try to make it as
close to that as possible.  With some dedicated resources, we have
used preemptible jobs (see below) for the "common" access.


Preemptible jobs
----------------

One solution to many of the things above is to make jobs in partitions
**preemptible**, which means that if a higher priority jobs comes
along, a currently running job can be killed.  It's killed with a
short grace period to save its state (which it should be designed to
do) so that it can be resumed.

Preemptible jobs are great since they allow all the otherwise-unused
resources to be scheduled.  However, it can be a big step up with
effort to manage saving state and scripting the continuation of jobs
at scale.  We want new users to have some easy onboarding path, so
we will always make preemptible jobs opt-in.  We expect that big users
will have enough benefit to adapting to preemptible jobs, which helps
to improve efficiency for everyone else who can't.

If you can adapt your work to use preemptible jobs (and you are using
a cluster that has them enabled), then we encourage you to make use of
that option.


Summary of things that can be tuned per-partition
-------------------------------------------------

* Partition layout and overlaps
* Maximum runtime
* Maximum job size
* GrpTRESRunMins
* Preemptibility

Most importantly, while it may be possible to make some theoretically
perfect arrangement for maximum use and minimum waiting when not
expected, that can make the cluster usage much harder to explain.  So
we try to find a balance of those things and overall usability.  So
then, at the end, it becomes a trilemma: maximum resource usage,
resources always standing by for you, and usability.
