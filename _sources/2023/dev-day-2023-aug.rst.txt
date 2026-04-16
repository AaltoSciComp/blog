:blogpost: true
:date: 2023-10-30
:author: Richard Darst
:category: ASC


ASC development day, 2023 August
================================

We had another development day (previous:
:doc:`/2023/march-development-day`).  It went mostly like the last one, and
we have less important news for the world, but below is the summary
anyway.



Stats
-----

* We have about 1550 people with accounts, with 202 new account
  requests in the last six months.
* Most routine issues tend to be about software installation, which is
  good (this is the actually hard part, it's good people ask us).
* We are still on track for about 500 garage visits per year.  We
  don't try too hard to keep track of them all, we might get about 75%
  of them.
* The number of :external:doc:`interactive <triton/tut/interactive>`
  and :external:doc:`Jupyter <triton/apps/jupyter>` users are increasing, while
  :external:doc:`Open OnDemand <triton/usage/ood>` is decreasing.  This
  is the wrong direction from what we'd like.  We will open
  OOD to connections from all of Finland to make this easier.



Triton v3
---------

Triton v3 is still on the way.  This isn't a new cluster, but a new
operating system which individual nodes will be migrated to slowly
(while maintaining the same accounts and data).  Most of this happens
in the background, but the change of base operating system images will
require most code to be recompiled, which will require attention
from many users.  The transition can be made slowly, both old and new
OSs will run for a time being.  There won't be a change in total
amount of computing power.

An upcoming blog post will discuss this more, and the effects on
users.  *Now is the time to start preparing.*  We still expect the
transition to happen sometime in the autumn.

We are thinking to merge home and scratch directories, to make a
common quota for both.  This would improve usability by reducing the
frequency of home quota affecting usage.  We'd welcome any other
usability suggestions.

Practically, we are using the chance to automate things even more,
which should make it easier to manage in the future.



Teaching
--------

Teaching has gone well.  For this academic year, we'd like to add back
in a few smaller, special-purpose courses (not just to teach them, but
also to get good quality video recordings for the future).

Goals:

* Developing and delivering the ":external:doc:`workflows
  <training/scip/ttt4hpc-2024>`" course with CodeRefinery
* Short courses to record (e.g. rerun of debug series, once a week,
  record and publish).
* Update :external:doc:`triton/usage/debugging` linking the
  different debugging course repositories.



LUMI
----

LUMI is the new EU cluster with plentyful GPU resources.  A user can
essentially get as many GPU resources as they need with no waiting,
but since the GPUs are AMD, there is some initial barrier.  Our
general feeling remains: "we won't recommend our users directly go and
use LUMI, but we recommend they talk with us first and we help them
use it".

Next steps:

* Continue encouraging users to contact us.
* RSEs will ask the top GPU user each week if they would like support
  with taking LUMI into use.  We'll go and do all the setup for them.
* Slide on infoscreens around the buildings?
