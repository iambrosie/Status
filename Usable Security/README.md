# Week 1

## HCI
Human-Computer Interaction, or HCI, is the study of how people interact with technology.
In HCI, the goal is to make sure people aren't working harder then necessary to use the technology that we've designed.
Applying HCI in order to achieve usable security:

* First step is understanding users, tasks and context.
* Second step is designing the system.
* Last is the evaluation step (in the usable security context, we're not evaluating the system's security, but *how easy it is for the users to use that system*), motivated by the fact that if people find the system too difficult to use, they'll find ways around or make insecure decisions.

## Usability
*Usability* is a measure and an understanding for how easy it is for people to use a system.
The following factors are considered when measuring usability:

  * Speed - how long it takes users to accomplish a task; mistakes are ignored (users are assumed to act in an optimal way); measured by timing.
  * Efficiency - how many mistakes are made in accomplishing a task; measured by counting errors (we may categorize the errors by severity).
  * Learnability - how easy it is for a user to learn to use the system; measured by repeatedly asking the user to perform a task and timing them (the process stops when the amount of time it takes them is leveling off).
  * Memorability - once learned, how easy is it for a user to remember how to use the system; measuring starts in a similar fashion to learnability but then wait for a certain amount of time and test again.
  * User Preference - concerned with what users like most; measured with questionnaires and surveys as well as conducting interviews.

## Tasks
*Tasks* are goals that users set out to accomplish in a system.
Usability of a system as a whole is too abstract of a concept. Thus, in order to evaluate the usability of a system, we create a list of representative tasks and evaluate the usability of those tasks according to the factors that we've discussed previously.
Tasks examples: log in to Facebook, check your credit card statement (a higher level task, with many subparts), read the headlines etc.
Common errors in task creation:

  * Too leading or too descriptive (you should think about the goal the user has in mind, e.g. logging in, and that should be the task)
  * Asking specific questions (you should consider reasonable goals users have)
  * Directing users toward things you want to tell them, not what they want to know (be careful in creating tasks; make sure that you're not directing people to information that you want them to look at; it should be something users intentionally want to see)

## Chunking Information
Human characteristics we should take into account when designing interactive systems:

Memory:

  * Of particular interest is the working memory, a.k.a. short-term memory; this is the part of our memories where we store information that we readily need to access in a quick amount of time.
  * George A. Milner (1956) - "The Magical Number Seven, Plus or Minus Two": working memory can hold 7 +/- 2 pieces of information; Broadbent (1975): 4 to 6; LeCompte (1999): 3; *Common Practice*: 4 +/- 1.
  * Chunking: working memory can hold 7 plus or minus 2, or 4 to 6 things; but if you can group things into meaningful chunks, you can remember 7 plus or minus 2 chunks or 4 to 2 chunks, as opposed to individual atomic elements.

## Mental Models
Mental models let us understand how users perceive systems.
When users come in to use a piece of software, they generally don't know how it works. Yet, often times, users are able to sit down and immediately begin using a piece of software by relying on mental models. 
This borrows knowledge from other parts of their life, including experience in the outside world and with other software they've used. That is, they have some models that they apply to the current piece of software and they can rely on their expectations and previous experiences to help guide them using the software.

The factors involved in developing mental models:

  * Affordances - elements of a system that show a user how they're supposed to be used. The components of Affordances: 
    * Mapping - discusses how certain functionalities will map to controls
    * Visibility - how to make functionality visible in a usable way
    * Feedback
  * Constraints - how a system can prevent us from doing things that we shouldn't and how the design of it can encourage us to do things the right way.
  * Conventions - describe a common understanding of what something means.

## Additional Readings
* [Usability 101] (http://www.nngroup.com/articles/usability-101-introduction-to-usability/)
* [Human-Computer Interaction] (http://www.prenhall.com/behindthebook/0132240858/pdf/Kendall_Feature2_Human_Computer_Interface.pdf) chapter in Systems Analysis and Design by Julie E. Kendall and Kenneth E. Kendall

# Week 2