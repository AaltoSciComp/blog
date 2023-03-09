:blogpost: true
:date: 2023-03-07
:author: Richard Darst
:category: ASC


ASC development day, 2023 March
===============================

We recently had an internal "development day", which is a our new name
for getting together to talk about longer term plans.  This is our
second "development day".  Overall, it went well, and we think that we
are on an overall  good path.  There are three particular focus areas
for the future:

1. **Teaching:** This was also a focus last time, and probably will
   still be in the future.  We are overall happy with our decision
   last time to focus less on many small/medium courses, and instead
   focus on large, collaborative courses and then focused,
   individualized support for advanced use cases.  Smaller courses
   happen mainly when we see specific needs that can't be filled other
   ways (or we make them large, open, collaborative courses if there
   is a broad need).

2. **Triton v3:** The software/OS/management side of our cluster will
   be almost completely reworked in the next year (we aren't getting
   rid of any hardware just for this).  This will take a fair amount
   of our time, but is needed because existing systems are starting to
   show their age.

3. **LUMI usage:** LUMI is a flagship project of EuroHPC and provides
   huge resources available to the same people that can use Triton.
   Triton is still needed for ease of use of everyday projects, but we
   should actively look for people who can benefit from it and help
   them port to there.  Our recent evaluations lead to the conclusion
   that our porting help is still needed there.



Teaching
--------

Teaching has long been one of the pillars of ASC's support.  It's
still needed, but the focus seems to be changing.  No longer is a room
with 10-20 (or ever 50) people considered a lot.  People seem both
more able and willing to find advanced material themselves, and more
in need of basic principles (git, Python for SciComp, etc).  Perhaps
this is also partly caused by the remote work period emphasizing how
all this material is available online anyway.  Our basic philosophy:

* **Focus on large courses for new researchers**, for example using
  the `CodeRefinery MOOC strategy
  <https://coderefinery.github.io/manuals/coderefinery-mooc/>`__.
  This reaches the most people, helps the beginners the most,
  produces high-quality open source material for asynchronous
  reference, and has good possibilities for co-teaching.
  Example include `CodeRefinery
  <https://coderefinery.org>`__, our `SciComp/HPC kickstart course
  <https://scicomp.aalto.fi/training/scip/kickstart-2022-summer/>`__,
  and `Python for Scientific Computing
  <https://aaltoscicomp.github.io/python-for-scicomp/>`__.

* **Advanced, one-on-one, or small-group support** via `SciComp garage
  <https://scicomp.aalto.fi/help/garage/>`__ and the `Research
  Software Engineering service <https://scicomp.aalto.fi/rse/>`__.
  This isn't just for projects, but is also a useful service for
  people learning from other advanced material in their work -
  basically, we work as mentors.  One-on-one support is both more
  rewarding for us and probably more useful to the user (relative to
  time demands on both ends).  Anyway, advanced courses often aren't
  offered right when people need them, so we are left in this position
  anyway.

* **What about small/medium-sized courses, and advanced courses?**

  * The first two points above squeeze out medium-sized courses for
    the most part, in our opinion.  By the time our audience is an
    intermediate or advanced level, they seem to be able to figure
    things out themselves + ask for help when needed - if they can
    figure out what they need to do.  This point deserves further
    study, though.  Instead, we point to other existing material.

  * We will make sure that we have good recommendations for advanced
    self-study courses and generally chart out the resources so that our
    users don't have to.  This is mostly done by our `Hands-on Scientific
    Computing <https://hands-on.coderefinery.org>`__ course.

  * In the past, we have supported community members to give courses on
    topics of which they are experts.  Continue this as appropriate (see
    the next point).

  * Continue the possibility of **on-demand courses** taught by us if
    someone requests them, and other smaller courses if we see a strong
    need.  Contact us!



Triton v3
---------

Triton is our HPC cluster, and is notable for being a Ship of Theseus:
it's continually upgraded while being the same cluster.  This has
resulted in the software running it getting a bit out of date.  This
software was originally developed as broader partnerships, and as
these partnerships have changed, we need to take more responsibility
for it ourselves.

Users shouldn't see any major change from this, though part of it is
improving our (user) software installation tools, which should make
increased responsiveness to software installation requests.


LUMI
----

As said above, Lumi is a significant resource, yet our users have not
come to us asking for our help in using it. Over the past six months, we
have found some Triton users who would benefit from it and helped
extend their workflows to work on LUMI.  We do this by first testing
some applications ourselves, then looking at Triton usage for large
users and reaching out directly.

Currently our focus is on GPU-intensive applications, which is made
more interesting because LUMI has AMD GPUs.  We've gotten local AMD
GPUs for our own testing and in general are well prepared to support
this.

While LUMI is a HPC system and has a typical HPC system interface, it
serves so many different users that the software stack is very
limited, so that most users need to install their own software and
figure out how to run it on AMD GPUs.  This is why we recommend most users
access LUMI through us (we're paid to save you time, after all), though
of course anyone interested can use it directly.
