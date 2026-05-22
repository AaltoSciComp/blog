:blogpost: true
:date: 2026-05-21
:author: Richard Darst
:category: ai


Thoughts on an Aalto AI strategy
================================

Much has been said about AI strategies for Aalto.  Yet, as our
:doc:`last post </2026/what-is-ai>` talked about, AI can be
anything - thus it's hard to write a strategy.  This post is about
what we, Aalto Scientific Computing / ASC, think should be considered
in such a strategy.

Read :doc:`last post </2026/what-is-ai>` if you want some
background.


.. admonition:: General steps for AI strategy

   * Minimize the use of the term "AI" except for branding purposes.
     Be specific about intention in communication.
   * Providing computing and deep learning specialists who can advise
     on "what AI means" and how to actually incorporate it into
     projects (beyond chatbots).


Consumer of AI tools
--------------------

One side is being a **consumer** of AI products developed by others.
Do we want to buy all the latest tools to generate content?  Do we
want to buy tools to help us make decisions (probably wrapped in
proprietary logic?).

These tools definitely have some use, given the huge amount of tools
that generate content (writing, code, images, etc).  Still, for this,
we are a follower and paying others for the privilege.

.. admonition:: Steps for consuming existing AI tools

   * Any AI strategy should consider under what conditions, and with
     what budget, for buying outside tools.
   * A plan for future cost increases of AI tools, including
     possibility of moving to local resources where appropriate.
   * If this is part of the strategy, there should be a way to do
     these procurements rapidly, otherwise we are not only a follower,
     but a follower of the followers.
   * Training with emphasis that "AI" is prediction and not "actual
     intelligence" with decisions made opaquely by the provider.
   * Support for advanced use (especially for coding), when AI code
     generation leads to problems which users can not solve
     themselves.


Developing platforms
--------------------

In addition to procuring tools, we can internally build our own
platforms optimized for our own internal use as tools.  We can take
various bases:

a) purchased AI inference in the cloud (subscription cost but no
   capital cost), and
b) open-weight models which we can run fully locally (capital cost but
   no subscription cost).

Developing our own platforms has the advantage of providing more local
sovereignty: they have more data and decision-making fully within our
control, including the possibly of running fully on-premises.
Services can be more easily transferred from (a) to (b) in the future
to control costs and sovereignty, as needed.

.. admonition:: Steps for developing AI platforms

   * A local development process which can rapidly iterate and deploy
     platforms before they become obsolete.  (Current small-scale
     development rules are far too slow.)
   * Investment in the hardware, data, and human resources needed to do
     this development.  Prepare for a future where cloud AI inference
     prices increase and it becomes necessary to move some work to
     local hardware.
   * A clear understanding of the AI act and the difference between
     something using AI under command of a human and a AI system
     (which is autonomously making decisions and affecting the
     environment).
   * Support in how to think about both using and developing AI tools,
     instead of being a consumer.

   Implementation: Drastic reform the small-scale development process
   and broaden Research Software Engineer support to more departments.


Developing AI methods
---------------------

Finally, we develop new AI methods: either deep learning methods, or
applying deep learning methods to new fields.  This is the groundwork
needed for platforms and tools of the future, and is probably what is
meant by "being an AI leader".  The revolution isn't just replacing
human work by generated content, but being able to see patterns in new
fields.

Method develop can be computer science-y stuff, where you are really
developing a new method (probably for some application but the novel
result is the deep learning).  Or it can be for another field,
developing a new method in their field using AI (where the novel
result is in the other field).  Real magic can happen when these two
halves work together.

.. admonition:: Steps for developing AI methods

   * Good computational resources for development, both powerful and
     with good user interfaces for people who aren't computer
     scientists or physicists.
   * Computing support, who can help guide researchers from diverse
     fields to the right {AI methods, computing resources, software
     frameworks}.
   * Research software engineering support for those applying AI to
     new fields.

   Implementation: focus on Aalto's Triton resource (designed for more
   usability across broad fields) and Aalto Research Software
   Engineers (which helps with Triton *and* other platforms).
