:blogpost: true
:date: 2026-05-21
:author: Richard Darst
:category: ai


Thoughts on a practical AI strategy in research
===============================================

Much has been said about "AI strategies": increase AI development and adoption in higher education institutions. 
Yet, as our :doc:`last post </2026/what-is-ai>` discussed, since AI can be
anything, it's hard to write a useful strategy.  This post is about
what we, Aalto Scientific Computing / ASC, think should be considered
in such a strategy in research.

Read :doc:`last post </2026/what-is-ai>` if you want some
background.


.. admonition:: General steps for AI strategy in research

   * Support AI development and adoption from core methods to standalone AI tools
   * Minimize the use of the generic term "AI".
     Be specific about intention in communication.
   * Provide computing and machine learning specialists who can advise
     on "what AI means" and how to actually incorporate it into
     projects (beyond chatbots).
   * Lower the barrier to testing open-source AI tools in researchers' workflow


We can think of an AI system as a layered structure. This helps us support the development and adoption of i) new AI methods and AI models, ii) AI components and platforms that turn the methods into building blocks for applications, iii) AI tools that connect the components to the interfaces and workflows used by researchers

Developing AI methods and AI models
-----------------------------------

Researchers develop new AI methods and AI models, often in the field of machine learning. This is the groundwork
needed for platforms and tools of the future, and is probably what is
meant by "being an AI leader".  The revolution isn't just replacing
human work by automation, but being able to see patterns in new
fields.

Method/model development can be the core computer science-y stuff, where you are really
developing a new machine learning method. Or by using ML methods/models in various fields of research, 
researchers can develop new ways of looking at research data.  Real magic can happen when these two halves work together.

.. admonition:: Steps for developing AI methods

   * Good computational resources for development, both powerful and
     with good user interfaces for people who aren't computer
     scientists or physicists.
   * Computing support staff, who can help guide researchers from diverse
     fields to the right AI methods/model, computing resources, and software
     frameworks.
   * Research software engineering support for those applying AI to
     new fields.

   Implementation: focus on Aalto's Triton resource (designed for more
   usability across broad fields) and Aalto Research Software
   Engineers (which helps with Triton *and* other platforms).


Developing AI components
------------------------

Core machine-learning methods can be difficult to integrate in applications: if one researcher is planning to use a local large language model interactively, it would be inefficient to reserve a large amount of computational resources just for a single user. Developing AI components is the key here to enable the adoption of AI methods. 

AI components can be proprietary or open source. For example in the case of large language models:

a) purchased AI inference with proprietary models in the cloud (usage costs but no
   capital costs), versus
b) local AI inference with open-weight models (capital costs but
   no usage costs).

Developing our own AI platforms has the advantage of providing greater local
sovereignty: data and decision-making are fully within our
control. Services can be more easily transferred from scenario (a) to scenario (b) in the future
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

While it is important to test and use the state of the art proprietary AI tools, an ecosystem of open source tools with a local AI components has merged and it is part of our strategy to support it. You can code using Claude Code and pay real money for tokens (and live with the risk of loss of confidentiality), or use a local LLM endpoint which can perform as well as a proprietary alternative.

.. admonition:: Steps for adopting existing AI tools

   * Any AI strategy should consider under what conditions, and with
     what budget, it should encourage buying proprietary tools.
   * Procurements should happen rapidly, otherwise we are not only a follower,
     but a follower of the followers.
   * The strategy should contain plan for future cost increases of AI tools, including
     possibility of moving to open source alternatives where appropriate.
   * The barrier to using open source AI tools should be as low as possible to ensure  transparency   
     and maintain the confidentiality of tool use
   * AI literacy and competence are needed to understand the limitations of these tools: the opaque logic of the proprietary tools, the potential
     loss of confidentiality, and the new risks introduced that can erode research integrity and compliance.
   



.. raw:: html

   <pre class="ai-strategy-ascii">
             LEVELS OF PRACTICAL AI STRATEGY IN RESEARCH


     +------------------------------------------------------------------+
     | LEVEL 1: DEVELOPING AI METHODS & AI MODELS                       |
     |                                                                  |
     |  core ML groundwork -> new methods/models -> novel research      |
     |                                                                  |
     |  Support: computing resources, RSEs, ML specialists              |
     +-------------------------------+----------------------------------+
                                     |
                                     v
     +------------------------------------------------------------------+
     | LEVEL 2: DEVELOPING AI COMPONENTS AND PLATFORMS                  |
     |                                                                  |
     |  methods/models -> reusable blocks -> shared services            |
     |                                                                  |
     |  Choices: cloud vs local, proprietary vs open models             |
     |  Aim: sovereignty, scalability, rapid deployment                 |
     +-------------------------------+----------------------------------+
                                     |
                                     v
     +------------------------------------------------------------------+
     | LEVEL 3: USING AI TOOLS                                          |
     |                                                                  |
     |  tools -> workflows -> adoption                                  |
     |                                                                  |
     |  Needs: AI literacy, risk review, open source options            |
     +------------------------------------------------------------------+


           Across all levels: people + hardware + support + competence
   </pre>
