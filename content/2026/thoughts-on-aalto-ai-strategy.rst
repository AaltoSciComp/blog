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


Consumer of AI tools
--------------------

One side is being a **consumer** of AI products developed by others.
Do we want to buy all the latest tools to generate content?  Do we
want to buy tools to help us make decisions (probably wrapped in
proprietary logic?).

These tools definitely have some use, given the huge amount of tools
that generate content (writing, code, images, etc).  Still, for this,
we are a follower and paying others for the privledge.


.. admonition:: Steps for consuming AI tools

   * Any AI strategy should consider under what conditions, and with what
     budget, for buying outside tools.
   * If this is part of the strategy, there should be a way to do these
     procurements rapidly, otherwise we are not only a follower, but a
     follower of the followers.
   * Training in using AI tools responsibility.
   * Support for advanced use (especially for coding), when AI tools
     lead to confusion which users can not solve themselves.


Developing platforms
--------------------

In addition to procuring tools, they can be internally developed.  We
can take various bases (purchased AI inference in the cloud, or
open-weight models which we can run locally), and build our own custom
platforms (optimized for our own use).

This has advantages of providing more local sovereignty: they can be
run fully on-premises (no outside dependence or subscription costs).
If it's built on a cloud AI inference, at least the raw data is
sovereign (it can be on-premises), and many of these can be
theoretically transferred to run on-premises at a later time.

.. admonition:: Steps for developing AI platforms

   * A local development process which can rapidly iterate and deploy
     platforms before they become obsolete.  (Current small-scale
     development rules are far too slow)
   * Investment in the hardware, data, and human resources needed to do
     this development.  Prepare for a future where cloud AI inference
     prices increase and it becomes necessary to move some work to
     local hardware.
   * Training in how to think about both using and developing AI tools.


Developing AI methods
---------------------

Finally, we develop new AI methods: either AI methods, or applying AI
methods to new fields.  This is the groundwork needed for platforms
and tools of the future, and is probably what people think about for
"the world being revolutionized with AI".  The revolution isn't just
replacing human work by generated content, but being able to see
patterns in new fields.

Method develop can be computer science-y stuff, where you are really
developing a new method (probably for some application but the method
is the deep learning).  Or it can be someone in another field,
developing a new method in their field using AI (where the primary
purpose is to support the other field).  Real magic can happen when
these two halves work together.

.. admonition:: Steps for developing AI methods

   * Good computational resources for development, both powerful and
     usable by people who aren't computer scientists or physicists.
   * Computing support, who can help guide researchers from diverse
     fields to the right {AI methods, computing resources, }
   * Research software engineering support for those applying AI to
     new fields.


A metaphor
----------

In :doc:`last post </2026/what-is-ai>`, we proposed a metaphor of
"when cars became mass produced and more reliable, there was more
driving.  While people had to know less about maintaining cars, but
more people had to know how to drive and work around cars."  In this
metaphor, transportation became cheaper and more powerful (yet we
still definitely don't want cities designed just for cars).

Our goal is not more AI ("cars").  Our goal is cheaper and better
transportation (actually useful tools, and computational methods).
Don't think of ways to use AI.  Think of all the expanded computation,
more rapid prediction and decisions, and (if you want...) content
generation that is possible.
