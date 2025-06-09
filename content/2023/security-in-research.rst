:blogpost: true
:date: 2023-11-16
:author: Richard Darst
:category: security, infrastructure


IT Security needs in research: Science-IT recommendations
=========================================================

At Science-IT, we are work at the interface between researchers and
university IT systems.  One common issue we hear about is the worry of
IT Security practices and how it relates to, and can interfere with,
research.  This blog post is designed to address some misconceptions
and provide recommendations to both sides to improve research and
security.


The current state
-----------------

Aalto policies classify data into four categories (the following table
is focused on research use cases):

.. list-table::

   * * Public
     * Data which can be released publicly.  Since we should be doing
       `Open Science
       <https://www.aalto.fi/en/open-science-and-research>`__, most
       research data should eventually be public ("As open as
       possible, as closed as necessary").

   * * Internal
     * Data which shouldn't be released but doesn't have any major
       harm or legal consequences if it was released.  Not much
       research data should be under this category: either it needs to
       be private and it should be confidential, or it *could* be
       released under the principles of open science (but just isn't
       released yet).

   * * Confidential
     * Most data which has some legal or contractual data to be
       private: personal data, data under NDAs, trade secrets, etc.

   * Secret
     * Data such as health data, sensitive personal data.

There are university-level guidelines, but they say that all
unpublished research data is "confidential".  Over-generalizing means
that, in essence, the classification is up to the expertise of the
researcher.



Recommendation: avoid over-classifying data
-------------------------------------------

One common problem is the over-classifying of personal data. As one
person once said:

    We asked research how important and private their data is.  They
    said extremely important and confidential.  When we said all the
    requirements this mean for their handling of data, they then
    reported that their data wasn't very important or confidential.

This shows the natural tendency to over-classify data.  When
consulting the Aalto guidelines, it seems that any research data would
be confidential.  At the same time, much of this data will be
published, thus making the only risk that someone would see it before
a publication is ready, as opposed to after.  This is usually entirely
manageable, given that the researchers could just as well decide to
publish the data earlier.  In fact, in "radical open science" and
other open-source projects, intermediate results are immediately
released for feedback and collaboration.

Over-classifying data is damaging because it creates a waste of
resources handling data too strictly, and losing opportunities of
collaboration or using new tools.  A low classification level does not
mean that data *must be shared right now*, or that it can't be treated
more strictly as appropriate.  It just means that you don't have to do
*everything* at the higher classification level.

Note that, if you ask around university services, you can hear advice
that "if research should be treated as public (it has no reason to be
confidential), yes, you can treat it as public data."  This isn't
written down anywhere, but is the only reasonable interpretation for
modern science.

Recommendations:

* Research data is not treated as a single type of data but each
  dataset be treated as it deserves to be.  Common recommendations
  would be **public** if it is intended for publication and has no
  particular reason not to be made public, **confidential** for most
  other cases.  This does not imply any particular data sharing.

* Classification guidelines for research data should specify that
  research data can be in the appropriate category, by stating "public
  = research data which doesn't have [list of reasons to be
  confidential]"

* Researchers self-classify their data at the minimum required level,
  but use the best possible tools.  The tools recommended for
  confidential data generally have good usability and other good
  features (backups and so on).

* Open Science advocates promote early data sharing for it's security
  advantages.  The Open Science team improves documentation about
  classification of research data.

* Data Agents learn more about security practices and give feedback
  from more research fields, and can serve as a front line
  recommending secure practices.  The security team takes into account
  Data Agent feedback so that researchers are not afraid of required
  practices.

As an aside, integrity of data should be separated from
confidentiality: research data must be preserved for validation, but
often sharing the data on a reputable repository is the best way to
accomplish that.  Integrity requirements should not limit access or
use of tools not rated for confidential information.



Recommendation: more agile service offering
-------------------------------------------

Research moves fast, but security evaluations move slowly.  Security
evaluations by their nature can only be done on very few services and
tools, but the worldwide selection of research needs are far, far
higher.  Security approval requires one-to-one agreement between every
service provider and the university.

Services suitable for "public" data (more liberally interpreted for
research data as seen above) should be much more rapidly evaluated.  A
service which a researcher would otherwise sign up for and use
themselves should have a relatively low threshold for approval.

Recommendation:

* Public data can be used in any services.

* Public service security evaluations focus less on one-on-one
  confidentiality agreements but instead on other considerations, such
  as other ethical considerations. (if evaluation of public services
  is needed)

Without the above, either research is very much held back, or
researchers hold security policies in general disregard.  A clever
researcher would fake-"publish" data by posting it on their webspace,
but not sharing the link with anyone, so that data is now public.

Obviously, any user of random online services may be giving their own
personal data to that service.  That has to be an individual choice,
and not required, but also not prohibited.



More agile support of research development
------------------------------------------

Currently, most research development




Thoughts on university's role
-----------------------------

We acknowledge that, as a public institution, there may be national
policies that require strict treatment of research data.

Recommendation:

* If Aalto University is serious about treating itself as a strict
  government institution, it should be mentioned at the hiring stage
  to discourage those who do research faster than the speed of
  security evaluations.

Researchers should not be placed in a situation where they expect to
do research at a world-class university but are working in an
environment more like a slow-moving governmental institution.  The
disconnect in environment vs policies results in a more active
disregard of university policies in places they are actually
important.



Other notes
-----------

The security landscape in Finland is different than in other
countries, especially for students.  Student have a study *right*, not
*privilege*, and we can not require students to use services which
haven't been evaluated and have a specific data protection agreement
with the university.  The "public service" comments above can not
apply to any teaching work.
