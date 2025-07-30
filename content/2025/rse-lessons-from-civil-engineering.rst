:blogpost: true
:date: 2025-07-31
:author: Richard Darst
:category:


RSE lessons from Civil Engineering
==================================

I have had a long-running metaphor of {academic researchers, research
software engineers} being like {architects, structural engineers}.
The basic idea is that coming up with interesting and worthwhile
ideas/designs is a distinct field from giving ideas "structural
integrity" (=reproduciblity and technical rigor).

I've been thinking of this metaphor a lot, and decide to learn more.
Thus, I read the book `Civil engineer's handbook of professional
practice <https://search.worldcat.org/title/716208794>`__, by Karen
Lee Hansen and Kent Zenobia (2011, first edition) (but there is a
second edition).  I expected for the book to give me various insights
that could be useful for developing a team of research engineers.  It
was about 500 pages, so not exactly recommended reading for others,
but I certainly got very many insights and am glad I read it.

Below, I quickly summarize each chapter, say any particularly
interesting things I learned, and **in bold tell any recommendations
to our team** based on the chapter contents.



1 Introduction
--------------

This chapter talks about the goals of the book and the education of
engineers in general.  For example, it talks about how accrediting
organizations for universities have tried to define what should be
part of various curriculum at different levels: bachelors (4-year
degree) level, masters, and professional experience.  These can be
defined in terms of Blooms Taxonomy levels, for example.

My main take-aways are about how there are people who think about the
skills which should be learned, a lot like some people have tried to
define RSE training programs.  The most notable thing for me is how
plenty of the skills are only learned by professional experience after
graduation.  Somehow, this matches with my feeling: I don't have a
direct desire to make a RSE undergraduate curriculum, but people can
learn basic skills of computational science during a variety of
undergraduate curricula.  I am currently more focused on the practical
training after becoming a computational researcher or starting a RSE
job.

**I would now want to be more involved in RSE curriculum learning
goals, but not too much.  This chapter gave me lots of inspiration for
how to onboard future research engineers to our team, especially those
who join at a more junior level than our current staff.  I think the
hardest part isn't so much about basic skills, but how to work in a
team to whose mission is supporting science.**



2 Background and History of the Profession
------------------------------------------

This chapter gives a history of civil engineering.  "Civil" originally
meant as opposed to military, though now it means construction.
Before modern times, there wasn't a distinction between architects and
engineers, or military and civil engineers.  There were just engineers
who did it all.  The engineering profession came about because
construction became more complex during the industrial revolution -
more specialization was needed.  There is a lesson for RSEs here:
computational science has become that complex that everything a person
needs can't be included in every undergraduate program.

The book mentions how the earliest engineering projects in Mesopotamia
don't survive, because they didn't have many stones, or fuel for
firing bricks, that could create long-lasting structures.  There's a
metaphor to research software which is lost to time because it wasn't
made sustainable enough because the developers didn't use the right
tools.

These days, there is advanced engineering education with a strong
scientific basis and many career paths.

**This section makes me feel good about my architects vs engineers
metaphor and gives me some new ideas to add to the metaphor.  We
should emphasize that advancing technology means that more career
specialization is needed.**



3 Ethics
--------

Engineering ethics is important because bad engineering can harm
society.  (I forget which chapter I read it in, but somewhere in this
book it mentioned how in ancient times, if an engineering work killed
or harmed someone, the engineer would be killed or harmed similarly.
That's some real pressure to get it right.)  Different professional
organizations have their own codes of ethics.  They are divided to
fundamental principles (fundamental doctrines) and fundamental canons
(broad principles of conduct).  Common things they include are
integrity, impartiality, fairness, corruption.

This chapter also talks about licensing some (getting a license to
practice and sign off on projects as the ultimate guarantor).  Imagine
if academia was so tightly controlled that a professional in research
integrity had to personally sign off on the scientific rigor and
reproduciblity on each scientific output (under the actual threat of
damage and investigation).  Considering the reproduciblity crisis,
this is a huge gap between the expected rigor of civil engineering and
academic publishing.

**It's appealing to think of formalizing a RSE code of ethics,
licensing, and signing off on results.  In practice, though, I think
the harm we can do is much smaller and we can't justify being as
strict - the risk reduction isn't worth the slowdown.  Academia has
plenty of ethical issues, and those should be addressed within
academia first (not as a separate RSE solution).**



4 Professional Engagement
-------------------------

A lot of this chapter is about defining work and negotiating
contracts, and different forms of project organization: for example,
is the designer the same as the builder?  Are they part of the same
contract or different contracts?  What are the different cost
structures and selection criteria?

There's a good lesson here about design-bid-build (designing and
building done by separate parties with separate agreements with the
owner) vs design-build (one organization designs and builds).  There
are plenty of places in science support where one organization gives
advice (for free) on how to do something, but doesn't help to do the
actual task.  This is like design-bid-build and the "builders" (either
within the original research group, someone they hire, or RSEs) may
not be in a good position to implement that advice independently.
*Our RSE team is more like design-build: we give advice, and we can
implement it.* The outcome is much better overall.

There's plenty about writing proposals (key points: don't forget to
understand the problem, client requirements, alternatives, and other
assistance) and contracts.

**In our team, we could spend more time at the beginning of projects
making sure that the scope of work and expected final state is well
understood at the beginning - some of our projects are ad-hoc now, often
diving in without fully understanding the results.  We shouldn't
become too strict, though: unlike civil engineering, research needs
to be far more agile.**

**We should learn how to write a better project plan (to confirm with
the customer) that is also as short and has the least waste.  Learn
how to narrow down to the customer's goals more quickly (which is
harder for us since computing is much more diverse in tools than civil
engineering).**



5 The Engineer's Role in Project Development
--------------------------------------------

This chapter talks about how the client, architects, civil engineers,
and contractors (builders) relate.  Design is split into schematic
design (the broad details and vision), design development (making it
more concrete), and finally construction documents (what a contractor
can build).  A collaborative design process (client, architect,
engineer) is very important.

The predesign process results in a "Statement of need", which allows
the client to internally approve the project to go forward.  This
states the problem, but not the solution.  The sooner the needs are
known, the more efficient the project will be.  Coming up with the
statement of need is itself an art and requires a detailed
understanding of the clients needs and application of engineering
thinking.  *The engineers give the statement of need, as the have
developed it, back to the client.*

The design phase has various checkpoints different fractions of the
way through.  Engineers can help the owner during the bid phase, help
supervise construction, and can help prepare operations and
maintenance plans.

**A good thing about our RSE team is that we know the people we serve.
We can easily know what people need (even if they don't know) without
an excessive amount of preparation, and work agile-y from there.  We
could do better about clarifying the statements of needs before we go
off and start working, though.**


6 What Engineers Deliver
------------------------

This chapter talks about the end product of engineering work.  Unlike
in our RSE team, where we build things ourselves, in civil engineering
the engineer usually delivers design documents, which someone else
(the contractor) will build.  Of course, there is engineering
supervision during the building and so on.  The end result of the
engineering work is various contract documents, such as drawing,
technical specifications, modifications to these, etc.  Not a
building.

Mostly, this chapter is too specific to apply to us, so I won't go
into details.  Most of our projects don't have a separate engineering
and building phase, and we don't have extensive design document
deliverables.  (We work in the design-build system, where we directly
implement the end product.  And our software projects are usually
small enough and agile enough that we don't make extensive design
documents, for better or for worse.)

However, it's worth pointing out that a construction (design) isn't
the only thing that engineers deliver.  They can deliver reports,
calculations, help with permitting, consulting to an owner about
dealing with other engineers/contractors, and more.  These are all
things that we as RSEs can do.

**We should keep in mind that RSEs can deliver more than just
software.  Projects and research have many components, and engineers
can help with all of them.  We can especially help with engineering
thinking during permitting, proposals, coming up with research
possibilities, and even sometimes analysis.**



7 Executing a Professional Commission—Project Management
--------------------------------------------------------

This chapter is about project management.  Why do projects need
management?  Because they can get so complex.  There's a good 2D
typology of {assembly, system, array} vs {low-tech, medium-tech,
high-tech, and super-high-tech}.  The first axis is for how complex
hierarchically the thing is, the second axis defines how available and
proven it is.  The higher up the axes, the more likely it is to need
dedicated coordination.  Projects are getting more about diverse
things working together in complex manners, instead of simple
breakdowns to various specialists.

What's a project?  Something to accomplish a goal in a fixed time
period (otherwise it's operations).  The project triangle is scope,
budget, schedule.  It's a trade-off between them and all three have to
be part of the negotiation with the client.

Who works on projects?  The owner (client), designer (decides what to
do), and builder (does it).  Often times other organizations give
advice on design without helping with the building. In a team, if's
the same project, all must work for the same customer and goal.  In
most of our RSE projects, the designer and builder are the same, but
we do often help come up with an idea and leave it to the owner to
build it themselves ("help you do it").

Projects have phases.  In civil engineering projects, the phases
include definition (predesign, 10% design), design phase (schematic
design, design development, construction documents), 100% design,
release to construction.  Each of these has a checkpoint where the
design should be reviewed with the owner (and presumably others
internally) to make sure it's on the right track.

Estimates are very important.  Estimates should be made as soon as
possible but will be refined over time.  Make sure to update them.
Prevent surprises.

A project management plan outlines how the project will be organized,
how everyone works together, and a whole lot of other important
reference information.  It's important to have all this reference
information in one place to keep everyone on the same page.

The role of a project manager is to basically take ultimate
responsibility for everything: ensure the project is done correctly,
ethically, client relationship, finance, business development, etc.
There is also a design leader who is responsible for the actual work
(who can be different from the project manager).

There is various discussion about tracking the progress of projects,
but for us RSEs we have good systems using repository hosting services
so I won't go into that.

Risk needs to be managed within projects: at least mentioned and
acknowledged, preferably allocated to the different parties.

**Realistically, most of our projects are too small to need a project
manager for their day-to-day work: there may be one RSE working, with
one or a few academics.  If a single project needs a dedicated
manager, it's probably of the academic side of the work.  At our size,
I manage the team itself, and I think the RSE staff can mostly the
work within the projects (more or less independently).  However, there
are many considerations which we can learn from, such as structuring
the various phases with checkpoints and having a written management
plan that also discusses how the project itself works.**

**The {scope, budget, schedule} triangle, risks, and project
management plan should more frequently be discussed at the start of
our projects.**



8 Permitting
------------

This chapter is about environmental permitting.  It talks about how
engineers dislike the process, think they know better and should be
independent, and on top of that have little training in managing
permitting.  Sound like academics?  A lot of the advice applies to
academia too.

Accept that permits exist for a reason (before them, there was
widespread societal harm).  Respect the agency staff implementing
permits: they are professionals and usually engineers.  If you do your
research first, understand the requirements, read the instructions,
etc. it will be much faster.  Initiate the permit process early.  Make
permits a first-order task, not a backend process (dedicated
permitting managers, consider permits from the bidding phase, engage
with the agencies, etc.).

To streamline permits, 1) prepare a combined project description with
all the basic information, which can be reused among each permit.  2)
don't skip step one.  3) Use this in each application.  This also
forces the advance planning, and it's OK if the project description
get updated.

However, I do have thoughts about this and our university's processes.
There are different aspects of "permits" in academics (ethics,
security, etc.), and all the processes are created internally, and
still you have to go repeating things over and over again for every
single form.  The "one combined project description" strategy doesn't
work.  Also, the ideal situation of "permit staff are experienced
engineers" isn't as true within our university environment (see
below).

**Our university should consider how to unify processes so that
materials can be reused much more than they can now (in line with the
recommendation of a unified project description for all permits).
Right now, there are many different processes, not unified and with a
lot of repeat work.  Also, unlike the description of agency staff
being experienced engineers, in our university the staff are often
lawyers or similar, thus they can't engage with advising on the actual
research projects.  If we hired more former academics/researchers to
be involved in permitting, it could go much more smoothly.**




9 The Client Relationship and Business Development
--------------------------------------------------

This chapter is about building relationships with clients and getting
work.  Engineering consulting firms are always looking for clients,
but luckily our RSE team is an internal team thus we have built-in
customers and funding.  Still, we need to keep our customers (academic
researcher) happy so they come back and give us good word-of-mouth
references.

The relationship is built on trust and commitment.  It's mediated by
communication.  That should result in understanding what the customer
needs, meeting their needs (scope/budget/schedule triangle) with
quality.  And this should be done with ethics and integrity.  It's
important to manage client expectations and not promise too much.

It's important to keep customers: easier to keep happy customers than
to find new ones.  However, you should also be careful about what
customers you choose: make sure you choose ones that match what you
can do and set the expectations well.  Networking, volunteering, and
other engagement helps to find customers.

Then there's business development, which is the work needed to find
new business.  All employees do this to some degree, but it larger
companies there may be some dedicated to it.  You find leads, do
background research, decide if you want to bid, and prepare the bid,
and hopefully get selected.  Coming back to the beginning, since we
are an internal team, we are often selected by default since we are
"free" or "at-cost".  But we shouldn't forget the work needed to
maintaining these customer relationships.

Conflict management with customers: collaboration, compromise,
co-existence, capitulation.

Our team is viewed excellently by our customers, but we cheat since we
work for free or below-cost as part of research support.  **Still, we
should all keep in mind the customer relationships.  We could be a bit
more picky about projects and make sure the expectations are set at
the beginning and not promise too much.  We should engage with the
broader scientific and user community to make scientific computing and
our services better known (rather than focus only on direct
marketing).**



10 Leadership
-------------

This chapter was a bit more about business leadership, rather than
project management discussed earlier.  This proposes that leadership
quadrants are (business strategy) (business economics), (technology),
and (public affairs/marketing).  Leaders plan, organize, lead, and
control.  Plenty more has been written about leadership outside of
this book and I don't think there's much more insight here.

**As our team gets bigger, I need to think more about how it's led and
how I can make sure everyone can have their voices heard.  I think
I've been doing better here lately, and think that many of these broad
visions things will occupy the next months or years of my time.  We
can start thinking of different types of leaders within the team.**



11 Legal Aspects of Professional Practice
-----------------------------------------

This chapter goes into details about the effects the legal system has
on professional engineers.  We are fortunate to not have to worry
about that too much, being focused on research with less stakes.

There are some good thoughts about concepts such as negligence,
liability and warranties.

It talks a lot about engineering contracts and problematic contract
terms.  It also talks about the main contract types, design-bid-build
and design-build, but there are even more (consultant to the client
separate from separate designer/builder, multiple prime, construction
manager, etc).  Then different types of contract, fixed price, cost
reimbursable, etc.

Then there is risk management.  You want good notes on everything to
prevent "you never said that..." situations.  One particular point is
that it's good to think about risk allocation (who bears the risk)
before you start, and it's usually best that risk is borne by those
most able to minimize it or be aware of it.  Then a bit about
insurance.  Then there's stuff about dispute resolution (litigation,
alternative dispute resolution).  Then anti-discrimination laws.

**We are fortunate that we work within one organization, so that we
don't have to deal with most of these legal aspects.  However, there
are good lessons about keeping good notes (which can help conflict
resolution later) and risk management (make sure it's discussed).
Finally, it's worth thinking about the (internal) formal
relationships: are we design-build.  Or design-consult?  Or is it a
multi-party relationship?  This sets the expectations.**



12 Managing the Civil Engineering Enterprise
--------------------------------------------

This chapter is about finances.  In addition to asking "can we do
it?", engineering firms should ask "should we do it?" with a go/no-go
decision process.  This can ask how well the work is understood,
client's expectations, degree of profitability, and risk factors.

There is plenty about costs of labor, overheads, multiplies, financial
reporting.

It also talks about human resources: who's available for what
projects?   What's their costs?  What's their career path and targets?

Then there is business development: finding clients and all, which
includes marketing and being involved in the community.

Our team is fortunate to not have to worry about per-project profit,
since we are also paid to maintain overall research quality.
**However, I think a "go/no-go decision" would be useful to us as a
way to make sure we understand everything before we dive in (even if
we always want to give some sort of "go", even if it's smaller than
requested).  And outreach doesn't have to just be marketing for
clients but can be general engagement with the community.**



13 Communicating as a Professional Engineer
-------------------------------------------

The chapter starts with a good general rule: "no surprises!".

Communication isn't just sending a message, but the reception and
understanding.  When communication is important, the sender should ask
for an acknowledgment (preferably including a summary as they
understand it).  When things are important (for example, spending huge
amounts to construct something), there is no room for mistake, and it
is the engineer's responsibility (not the client) to make sure that
communication goes through.  Don't forget the importance of
nonverbal/nonwritten communication (tone of voice, body language,
etc.)  Efficient communication is needed to stay profitable (it saves
time and improves the work).

It talks about how to use email.  I guess since the book was written,
this is now much more known, but there are some good points: be clean,
In the last 12 years this is sort of taken for granted.  Use good
subject lines.

Conflict resolution was also included here.  Conflict resolution
strategies include collaboration, compromise, coexistence, and
capitulation.

It then talks about report formats and so on.  As described in
previous sections, engineers have to produce lots of proposals,
responses to proposals, plans, etc. that aren't in use by our team.
In some ways, that's good for us, but there are some places where
better writing and planning could help us.  It's good to make sure to
include executive summaries at the beginning and recommendations at
the end of each document (most people don't have time to dig through
to find this or figure out what's going on).

One thing that struck me is how formal engineering communication can
be (with the idea that, you have to be very sure that you don't get
miscommunication or people remembering things differently).  For
example, it showed example of "phone call" and "meeting" forms, to
easily make written records of verbal interactions.  This can prevent
surprises later.

**I think communication should be one of our focus points.  With
users, we should make sure there are good records of what we discuss
and the plans we make.  We now have simultaneously editable web
documents, which is extremely powerful compared to 2011, and we should
use this more for project communication.  We should remember that time
is limited and communication needs to be clear and direct.  These
days, when I send emails, I always start with what I'm asking, and
then go into background.**

**Having "meeting record forms" is overkill, but I do think there are
some good lessons about being more clear in our communication with our
users.  Perhaps we can better use the online docs and continually add
notes of each meeting/interaction there.**

I have lots of other thoughts on communication from my other interest
in learning about accidents, but I'll talk about those elsewhere.



14 Having a Life
----------------

This chapter talked about work-life balance.  One example it gave is
that someone observed that, of their company's executives, most were
divorced and hand to pay more than half their salaries to their former
partners.  The executives' take-home salary was less than a starting
engineer.  The point is, maintain work life balance, avoid burnout,
etc. or else you will pay far more later.

It gives the key components as mind, body (eat, sleep, exercise), and
spirit (feelings and thoughts).  For the mind, it's important to
manage stress properly.

I'm happy with how our team works together so that everyone can
disconnect during vacation and work the right number of hours, but of
course a lot of that is Finnish working culture.  (I was entertained
by the irony that as I was reading this chapter, I was technically on
vacation.)  The academic system doesn't contribute to work-life
balance, and I hope that better RSE support of academics will help the
burn-out problem some, by making the work less overwhelming for
individuals.

**One of the best parts of our team is we get academic-quality people
but provide a much better work-life balance.  We should make sure this
balance continues in the future, and properly manage projects to
prevent them from affecting our lives.**



15 Globalization
----------------

Globalization is the reduction of barriers of mobility of goods,
capital, services, and labor.  It's more than just mobility: it is
mobility, simultaneity (things are available everywhere at once with
less time lag), bypass (multiple choices and being able to bypass
current structures), pluralism (not just one center dominating
things).

Interestingly, this chapter is the one that talks about the effects of
climate change (with the next being more about lifecycle cost
analysis).  Among many things that don't need to be restarted here, it
talks about how better project management and teamwork will be needed
to survive in the 21st century.

**I don't have any clever take-aways for us from this chapter.**



16 Sustainability
-----------------

I guess compared to 2011, we now think much more about sustainability.
Many things in this chapter are now well-known, or at least you
probably won't get much benefit from me repeating them.  Most of the
chapter is about design for sustainability.

It estimates that construction costs can be 5-15% of a facility's
lifecycle cost, design 1%, and operations and renovations most of the
rest.  Better design is the best way to reduce overall cost (and
environmental impact).  Likewise for software, more work at the
beginning can result in something much more usable later.  Systems
thinking is needed to improve sustainability.  Lifecycle costs
analysis include design/construction cost, maintenance costs, and
residual value at the end of the study period.

**RSE already uses software sustainability as a marketing point.  We
shouldn't forget this when talking about our benefits.**



17 Emerging Technologies
------------------------

This chapter isn't just about new technology, but how the way
technology and all interacts is getting more complicated itself.  How
it's going from "individual processes computerized/automated" to
"whole systems computerized/automated".  A lot of this is about data
exchange between systems and having a complete, up-to-date, view of
the designs and projects.

Another thing it talks about is "integrated project delivery",
basically different teams working together more closely than
otherwise.  Instead of relationships defined by contracts and
responsibilities, a combined team is formed.

It concludes a bit thinking about "engineering thinking": how to use
knowledge to make new innovation, and how new innovation makes more
new things possible.

**Our RSE team by definition is often helping others be on the
forefront of emerging technology, and we are often thinking about how
we should adapt to the next thing.**
