:blogpost: true
:date: 2026-04-27
:author: Richard Darst
:category: ai


What is AI? Everything, everywhere, all at once
===============================================

As Research Software Engineers (RSEs) in a university, we get lots of AI
questions and projects. But what is "AI" exactly? It can mean almost
anything, and it makes a bit of a problem when we may not even be
starting from a shared understanding of what a job is. Let’s discuss.

For us research engineers, a "real AI" project might mean "writing
Python code and optimizing deep learning training using a large computer
cluster". What we get for "AI" can be anything from that, to using an
existing model, to using a commercial language model via an API, to
writing web visualizations for AI data, to setting up student platforms
with Kubernetes, to advising on using chatbots.

In the end, "AI" is such an overloaded term that it can mean anything.
To better ask for help with "AI", it’s good to be able to specify in a
bit more detail what it is you need.

I think the effect of "AI" is to reduce the effort needed to use
computing tools, so the amount of computing people want to do increases.
These increases are proportional to all the usual computing projects we
get, even if the projects aren’t exactly deep learning training. Thus
the increased need for our team and its incredibly wide variety of
skills.

Types of AI
-----------

This blog post evolved out of talk at NoBSC 2026, where the issue of
"AI" meaning anything. In that talk, we thought of two broad categories:

"AI" can mean pattern matching and decision making. In this, you have
some input data and predict some output based on that.

"AI" can mean content generation, as in generating text or images.

You notice these two categories aren’t that dramatic? That’s because
they aren’t, it’s just that modern machine learning (deep learning) has
gotten so much better at it than even a decade ago.

(As you will see, these categories are more similar than you think.
These categories aren’t scientific - it’s just what we can say to make
it easier for our customers to define what they need.)


Pattern matching and decision making
------------------------------------

This is a traditional use of machine learning. Here, you take input data
and predict some output. This is usually done by having a lot of sample
input data and corresponding correct outputs, and training a model. When
you give the model new input data, it can predict the output. This is
known as "supervised learning".

This needs specific training data and the output model is usually
specific to that domain or model.

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

Just like it says, this is generating content. Examples could be
chatbots (generating text) or images based on some input. This has
become so widespread since 2022 that it’s easy to think that this is
"AI".

Under the hood, this is actually pattern matching, since it takes a
prompt, uses all the previous input data, and generates a predicted
output. There isn’t actually "intelligence" under the hood, and it’s all
limited by the power of the algorithms. It can be wrong, not useful,
etc.

Some people can use content-generating methods to make predictions,
which isn’t as refined as actual pattern-matching/decision-making
method, but because of the general-purpose nature of content generation,
it can work without much effort. One example I’ve heard of is using
large language models (LLMs) with an input such as "is this social media
post positive or negative sentiment? Answer with one word ‘positive’ or
‘negative’". You get a sentiment analyzer with very little work, that
has some large implicit knowledge background. The downside is it uses
much more computing resources and more chance of going off the rails
(hallucination, implicit biases, etc.). This is the power of these
so-called "foundation models" that can do many tasks.

Content generation is powerful, but has potential for misinformation or
misuse on a massive scale. One probably wants to be careful when using
content generation for predictive tasks.


Commercial platforms
--------------------

While not a category, there are also commercial platforms that do the
above things. They are set up to be easy to use by a broad audience. We
can help with these things, but most of the actual "AI" work is done.
ChatGPT’s early dominance in "AI" was probably caused almost as much by
figuring out a useful, usable interface for the general public as their
underlying "AI" technology.

Examples include the chatbots that everyone uses, coding assistants,
text summarizers, etc.


What you should do
------------------

If you, or someone, has an "AI" project, the first step is to dig deeper
and figure what it really is. rkdarst has an old saying, "explain it to
me again without any terms invented or made popular in the last ten
years". This helps to peel back these layers and get a description of
what is actually needed, and is probably quite useful when trying to
figure out what an AI project actually is.

We shouldn’t separate "AI" from computing skills in general. "AI" lets
people do more with less work, but it means everyone needs a higher base
level of knowledge (even about non-"AI" topics). Think back to when cars
became cheaper and more reliable. People didn’t have to know as much
about their intervals, but many more people had to learn how to drive
and interact with them. (We’re not saying we want our cities infested
with cars or AI). This is true even when the field of study isn’t
"computing". Don’t let "AI literacy" become "ChatGPT literacy", it is
literacy in computing, data, and problem solving.

Note: this blog post was written with zero "AI" content generation.


See also
--------

* `Fundamentals of secure AI systems with personal data -> What is
  artificial intelligence? <https://fundamentals-of-secure-ai-systems-with-personal-data-9cd9e2.pages.code.europa.eu/ch1.html#what-is-artificial-intelligence>`__


Appendix: Types of "AI" projects that Aalto RSE has done or heard about
-----------------------------------------------------------------------

Each sentence starts with the actual task and then explains why.

* .
* .
* .
* .
