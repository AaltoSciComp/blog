:blogpost: true
:date: 2026-04-27
:author: Richard Darst
:category: ai


What is AI? Everything, everywhere, all at once
===============================================

As Research Software Engineers (RSEs) in a university, we get lots of
AI questions and projects. But what is "AI" exactly? It can mean
almost anything, and it makes a bit of a problem when we and our
customers may not be starting from a shared understanding of what "AI"
is.  Let’s discuss.

For us research engineers, a "real AI" project might mean "writing
Python code and optimizing deep learning training using a large
computer cluster" or "does a Mixture of Experts-model produce better
accuracy compared to a traditional feed-forward network in my use
case?".  In practice, "AI" questions to us have included:

* Problems with web APIs
* Problems with PyTorch
* Problems with HPC libraries
* Problems with laws and regulations
* Problems with web servers
* Problems with Python installations

I think the effect of "AI" is to reduce the effort needed to use
computing tools, so the amount of computing people want to do increases.
These increases are proportional to all the usual computing projects we
get, even if the projects aren’t exactly deep learning training. Thus
the increased need for our team and a general increase in computing
and data literacy.

In the end, "AI" is such an overloaded term that it can mean anything.
To better ask for help with "AI", it’s good to be able to decipher it
down to the actual topic.  This post isn't about scientific computing
general, so let's look deeper below at what the core "AI" use cases
are:


Types of AI
-----------

This blog post evolved out of a colleague's talk at `NoBSC 2026
<https://aaltoscicomp.github.io/NoBSC/>`__, where they pointed the
issue that "AI" can mean anything, thus it isn't a good to speak of
"AI" projects without further clarification.  In that talk, we thought
of two broad categories for the actual uses of "AI":

"AI" can mean pattern matching and decision making. In this, you have
some input data and predict some output based on that.

"AI" can mean content generation, as in generating text, images, or
more.  This is, in fact, also a prediction of an output based on an
input prompt.

You notice these two categories are pretty normal things? That’s because
they aren’t, it’s just that modern machine learning (deep learning) has
gotten so much better at it than even a decade ago.  It's not
intelligence, it's predictions that seem human-like or better.

These categories aren’t scientific - it’s just what we use as a base
for discussion with our customers.


Pattern matching and decision making
------------------------------------

This is a traditional use of machine learning. Here, you take input
data and predict some output. This is usually done by having a lot of
sample input data and corresponding "true" outputs for that data, and
training a model. When you give the model new input data, it can
predict an output. This is known as "supervised learning".

This needs specific training data and the output model is usually
specific to that domain or model.  Deep learning can certainly find
patterns that humans or traditional machine learning can't - assuming
such patterns exist in the first place.

For an advanced example, an industrial plant has sensors monitoring the
whole process and records of each time it broke down. By using this
data, "AI" might be able to predict breakdowns more accurately that a
human or non-deep machine learning tools could. These types of uses are
relatively un-objectionable to society.

Other examples include things such as insurance companies using all of
their data to analyze claims and preemptively deny coverage to those who
think are more likely to get sick. Or using pattern matching to
approve/deny claims without a human taking responsibility. These have
much more societal impact and thus lead to lots of suspicion about "AI",
since it’s being used to diffuse responsibility.

Another type of pattern matching is classifying things without having
any true labels. This is called "unsupervised learning". One example
would be the "Netflix Challenge" where scientists tried to use watching
data to predict what would be relevant recommendations. It doesn’t
matter what the detected categories are, just that things go together.


Content generation
------------------

Just like the section title says, this is generating content. Examples
could be chatbots (generating text) or image generators based on some
input. This has become so widespread since 2022 that it’s easy to
think that this is "AI".

Under the hood, this is actually pattern matching, since it takes a
prompt, uses all the previous input data, and generates a predicted
output. There isn’t actually "intelligence" under the hood, and it’s
all limited by the power of the algorithms and the source data. It can
be wrong, not useful, etc.  Content generation is definitely *not* at
human-level, and does *not* have the wide background and task
knowledge of a human.  It is much faster, though.

Some people can use content-generating methods to make predictions,
which isn’t as refined as actual pattern-matching/decision-making
method, but because of the general-purpose nature of content
generation, it can work without much effort.  One example I’ve heard
of is using large language models (LLMs) with an input such as "is
this social media post positive or negative sentiment? Answer with one
word ‘positive’ or ‘negative’".  You get a sentiment analyzer with
very little work, that has some large implicit background knowledge.
This is the power of these so-called "foundation models" that can do
many tasks.  The downside is it uses much more computing resources and
more chance of going off the rails (hallucination, implicit biases of
input data, etc.).

Content generation is powerful, but has potential for misinformation or
misuse on a massive scale. One probably wants to be careful when using
content generation for predictive tasks.  The prevalence of generated
content and its potential for misuse is behind a lot of the backlash
to "AI".


Commercial platforms
--------------------

While not a category, there are also commercial platforms that do the
above things. They are set up to be easy to use by a broad
audience. We can help with these things, but most of the actual "AI"
work is already done.  ChatGPT’s early dominance in "AI" was probably
caused almost as much by figuring out a useful, usable interface for
the general public as their underlying "AI" technology.

So, while commercial platforms and purchasable tools may be easy, they
usually have very limited information about how they work (hidden
behind "AI" to make you think it's intelligent), and similar things
can be done locally given enough time and effort.  The delegation of
accountability (and thinking) to third-party platforms is also behind
part of the backlash to "AI".

Examples include the chatbots that everyone uses, coding assistants,
text summarizers, etc.


What you should do
------------------

If you, or someone, has an "AI" project, the first step is to think
deeper and figure what is really the goal.  rkdarst has an old saying,
"explain it to me again without any terms invented or made popular in
the last ten years".  This helps to peel back these layers and get a
description of what is actually needed, and is probably quite useful
when trying to figure out what an "AI" project actually is.  If you can
explain your project without saying "AI", you are well on the way to
solving it with "AI".

Also, we shouldn’t separate "AI" from computing skills in
general. "AI" lets people do more with less work, but it means
everyone needs a higher base level of knowledge (even about non-"AI"
topics). Think back to when cars became cheaper and more
reliable. Once cars became more common, people didn’t have to know as
much about their intervals, but many more people had to learn how to
drive and interact with them.  (We’re not saying we want our cities
infested with cars, nor AI).  This is true even when the field of
study isn’t "computing".  Don’t let "AI literacy" become "ChatGPT
literacy", it is literacy in computing, data, and problem solving -
and a healthy suspicion for details hidden behind jargon.

You certainly can benefit from "AI" without knowing all the details.
It's very hard to benefit from it without knowing your goal without
"AI".

*Note: this blog post was written with zero "AI" content generation.
My anonymous colleague has contributed some of the key ideas and
title.*


Definitions
-----------

* **Machine learning**: A field of study using statistical algorithms
  to learn from data and generalize to unseen data.
* **Deep learning**: Machine learning using multilayered neural networks.
* **Supervised learning**: Machine learning methods taking input and
  labeled "true" outputs as the training data.
* **Unsupervised learning**: Compared to the above, algorithms
  learning from input data which is unlabeled.
* **Training**: The process of iterating through the input data to
  find patterns, resulting in the trained model.
* **Model**: The learned parameters from input data and training,
  which can be combined with the right code to make predictions.
* **Application programming interface (API)**: An interface that makes
  it easy for a computer code to interact with something (as opposed
  to a human-optimized interface).
* **"Artificial intelligence"**: Did you think I'm going to give a single
  simple definition here?


See also
--------

* `Fundamentals of secure AI systems with personal data -> What is
  artificial intelligence? <https://fundamentals-of-secure-ai-systems-with-personal-data-9cd9e2.pages.code.europa.eu/ch1.html#what-is-artificial-intelligence>`__


..
   Appendix: Types of "AI" projects that Aalto RSE has done or heard about
   -----------------------------------------------------------------------

   Each sentence starts with the actual task and then explains why.

   * .
   * .
   * .
   * .
