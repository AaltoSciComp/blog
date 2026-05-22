:blogpost: true
:date: 2026-05-21
:author: Richard Darst
:category: ai


Thoughts on a practical AI strategy in research
===============================================

Much has been said about AI strategies to increase AI adoption in higher education institutions.  Yet, as our
:doc:`last post </2026/what-is-ai>` talked about, since AI can be
anything, it's hard to write a useful strategy.  This post is about
what we, Aalto Scientific Computing / ASC, think should be considered
in such a strategy in research.

Read :doc:`last post </2026/what-is-ai>` if you want some
background.


.. admonition:: General steps for AI strategy in research

   * Support AI development and adoptions from core methods to stand alone AI tools
   * Minimize the use of the generic term "AI".
     Be specific about intention in communication.
   * Providing computing and machine learning specialists who can advise
     on "what AI means" and how to actually incorporate it into
     projects (beyond chatbots).
   * Lowering the barrier to test open source AI tools in researchers' workflow


If we consider an AI system as a layered structure, we can enable the development and adoption of i) new AI methods, ii) AI components and platforms that turn the methods into building blocks for applications, iii) AI tools that connect the components with interfaces and workflows used by researchers

Developing AI methods
---------------------

Researchers develop new AI methods, often in the field of machine learning. This is the groundwork
needed for platforms and tools of the future, and is probably what is
meant by "being an AI leader".  The revolution isn't just replacing
human work by automation, but being able to see patterns in new
fields.

Method development can be the core computer science-y stuff, where you are really
developing a new machine learning method. Or by using ML methods in various fields of research, researchers can develope new ways of looking at research data.  Real magic can happen when these two halves work together.

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


Developing AI components
------------------------

Core ML learning methods can be difficult to integrate in applications: if one researcher is planning to use a local large language model interactively, it would be inefficient to reserve large amount of computational resources just for the single user. Developing AI components is the key here to enable the adoption of AI methods. 

AI components can be proprietary or open source. For example in the case of large language models:

a) purchased AI inference with proprietary models in the cloud (usage cost but no
   capital cost), versus
b) local AI inferece with open-weight models (capital cost but
   no subscription cost).

Developing our own AI platforms has the advantage of providing more local
sovereignty: data and decision-making are fully within our
control. Services can be more easily transferred from (a) to (b) scenarios in the future
to control costs and sovereignty, as needed.

.. admonition:: Steps for developing AI platforms

   * A local development process which can rapidly iterate and deploy
     platforms before they become obsolete with fast review process.
   * Investment in the hardware, data, and human resources needed to do
     this development.  Prepare for a future where cloud AI inference
     prices increase and it becomes necessary to move some work to
     local hardware.



Using existing AI tools
-----------------------

Finally, we want to empower **users** of AI tools .
There are many popular proprietary tools which embed an AI component and they always come with a price tag that users pay with real money or with the confidentiality of their data.

Do we want to buy all the latest AI tools to generate content or automate operations? (probably wrapped in
proprietary logic?). These tools definitely have some use, still, for this, we are a follower and paying others for the privilege. 

While it is important to test and use the state of the art proprietary AI tools, an ecosystem of open source tools with a local AI components has merged and it is part of our strategy to support it. You can code using Claude code and pay real money for tokens (and live with the risk of loss of confidentiality), or use a local LLM endpoint which can perform as well as the proprietary one.

.. admonition:: Steps for adopting existing AI tools

   * Any AI strategy should consider under what conditions, and with
     what budget, it should encourage buying proprietary tools.
   * Procurements should happen rapidly, otherwise we are not only a follower,
     but a follower of the followers.
   * The strategy should contain plan for future cost increases of AI tools, including
     possibility of moving to open source alternatives where appropriate.
   * The barrier to use open source AI tools should be as low as possible to ensure more transparency   
     and always maintain the confidentiality of the usage of the tool
   * AI literacy and competence to know the limitations of these tools: from the opaque logic of the proprietary tools, the potential
     loss of confidentiality, and the new risks introduced that can erode research integrity and research compliance.
   



.. raw:: html

   <pre class="ai-strategy-ascii">
             LEVELS OF PRACTICAL AI STRATEGY IN RESEARCH


     +------------------------------------------------------------------+
     | LEVEL 1: DEVELOPING AI METHODS                                    |
     |                                                                  |
     |  core ML groundwork -> new methods -> patterns in new fields      |
     |                                                                  |
     |  Support: computing resources, RSEs, ML specialists               |
     +-------------------------------+----------------------------------+
                                     |
                                     v
     +------------------------------------------------------------------+
     | LEVEL 2: DEVELOPING AI COMPONENTS AND PLATFORMS                   |
     |                                                                  |
     |  methods -> reusable blocks -> shared services                    |
     |                                                                  |
     |  Choices: cloud inference or local open models                    |
     |  Aim: sovereignty, scalability, rapid deployment                  |
     +-------------------------------+----------------------------------+
                                     |
                                     v
     +------------------------------------------------------------------+
     | LEVEL 3: USING EXISTING AI TOOLS                                  |
     |                                                                  |
     |  tools -> workflows -> adoption                                   |
     |                                                                  |
     |  Needs: AI literacy, risk review, open source options             |
     +------------------------------------------------------------------+


           Across all levels: people + hardware + support + competence
   </pre>
