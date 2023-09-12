:blogpost: true
:date: 2023-08-10
:author: Richard Darst
:category: triton


Preparing for new Triton
========================

Sometime in autumn of 2023 (e.g. September), we will do a major
update of Triton: updating the basic operating system, and thus almost
everything else.  There are big benefits to this: newer basic
operating system software, but also such a basic update affects almost
every user.  **For a short time, this will make a lot of work for almost
every user.  This post gives advance warning and a chance of feedback
of how to make the update most usable.**

This post is just advance warning and things to prepare already.  All
actual instructions will come later.


What will happen
----------------

We will update the basic operating system from CentOS 7 to something
else (Rocky 9 or Red Hat 9).  We've ordered all new management hardware
to make the backend more reliable and manageable.  Along with this
comes with an update of the software build system, which should allow
us to deploy software to our users even better.  We'll also update our
configuration management system for more reproducibility.

We also hope to think about the usability of the new system: remove a
lot of old options and add in new, simpler ways of doing what people
need.

All data and storage will remain the same, so there **is no big data
migration needed.**

The old and new clusters will be accessible at the same time (two
different login nodes), with the same filesystems mounted (same data
available) and some compute resources still available there, so that
people can slowly migrate.  But the old one won't stay running too
long, to avoid long maintenance effort or splitting of the resources.


Reproduciblity
--------------

The biggest problem with big cluster updates like this is
**reproducibility**: does you work from a month ago still work in one
month?  If not, this is a big problem.  It's even worse if there is a
much longer gap before you come back to it (paper revisions, anyone?).

You could say there are two things that can go wrong with a cluster upgrade or change:

- **Specific software/code that needs to be compiled and installed:**
  Software needs re-compiling for new clusters or new cluster OS updates.

- **Whole workflows:** you need to make all the pieces work together.
  Different paths and workflow managers may need updating.

What you can do:

- Manage any messes you have earlier rather than later.  It's better
  if you slowly clean up over time, so you can focus on the
  differences once the change happens.

- Know what software you are using.  It's easier for us to re-install something we
  have already installed when someone can tell us the exact name and version
  that they are using.
- `Tests for your software
  <https://coderefinery.github.io/testing/>`__.  Some way to validate
  that it works correctly.

- Contact `Aalto RSE <https://scicomp.aalto.fi/rse/>`__ for hands-on
  help supporting the transition.  Come to the `garage
  <https://scicomp.aalto.fi/help/garage/>`__ early and often.


Feedback and future usability
-----------------------------

If there are any annoyances about Triton that you'd like us to
consider for the upgrade, now is the time to let us know so we can
plan them.  **We especially value feedback on usability problems.**

Discuss with us in `our chat
<https://scicomp.zulip.cs.aalto.fi/#narrow/stream/6-triton/topic/feedback.on.new.Triton>`__,
or `open a Triton issue
<https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues/>`__.
