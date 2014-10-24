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

Human characteristics should be taken into account when designing interactive systems.

Of particular interest is the working memory, a.k.a. short-term memory; this is the part of our memories where we store information that we readily need to access in a quick amount of time.

George A. Milner (1956) - "The Magical Number Seven, Plus or Minus Two": working memory can hold 7 +/- 2 pieces of information; Broadbent (1975): 4 to 6; LeCompte (1999): 3; *Common Practice*: 4 +/- 1.

Chunking: working memory can hold 7 plus or minus 2, or 4 to 6 things; but if you can group things into meaningful chunks, you can remember 7 plus or minus 2 chunks or 4 to 2 chunks, as opposed to individual atomic elements.

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

## Design Methodologies

* Many design processes:
  * Iterative design - composed of the following stages: requirements, design, development and testing; the point is in all of these stages we're going back and forth and cycling around in a way that we allow ourselves to adjust any of the other stages along the way 
  * System centered design - doesn't involve a lot of users and resources; 
  * User centered design - focuses on the users and their importance to the systems; design is based upon a user's abilities and real needs, context, work, tasks; golden rule of interface design: "know the user"
  * Participatory design - a form of user centered design where the users are brought into the design process;
  * Designer center design - best described by the following quote by steve jobs: "it isn't the consumer's job to know what they want."

* Conclusions:
  * Users can give a lot of valuable insight for design by telling us about their tasks, context they're working in and their needs
  * We want design methodologies to support designers in coming up with new ideas
  * It's important to iterate in order to build better systems

## SSL Warnings

This session is based on the paper by Joshua Sunshine et. al. linked in the Additional Materials section.

Lessons:

  * Different interfaces can have major impact on the security behavior of users
  * What do we want users to do?
  * What do they need to understand in order to do that?
  * How can we make it more natural for them to do the "right" thing?

## Additional Materials

* [Crying Wolf: An Empirical Study of SSL Warning Effectiveness] (https://www.usenix.org/legacy/event/sec09/tech/full_papers/sec09_browser.pdf) by Sunshine, Joshua, et al. in USENIX Security Symposium, 2009
* [How to Brainstorm] (https://dschool.stanford.edu/groups/k12/wiki/3bae4/How_to_brainstorm__video_tutorials.html) by Royalty, Adam
* TED Talk on [Human-Centered Design] (http://www.ted.com/talks/david_kelley_on_human_centered_design) by Kelly, David


# Week 3

## Qualitative Evaluation

Designed to give you a sense of usability or to put you in the place of the user.

Amongst the techniques used in qualitative evaluation:

1. Cognitive Walkthrough

* Requirements
  * This is something you can do with an interface or a prototype of an interface.
  * You come up with a description of tasks.
  * You come up with a list of actions a user has to go through to complete that task.
  * You develop an idea of a user's background.

* What you look for
  * Will users know to perform the action?
  * Will users see the control?
  * Will users know the control does what they want?
  * Will users understand the feedback?

2. Heuristic Analysis

* When you do this, you follow "rules of thumb" or suggestions about good design.You go through the interface with a set of what you think are representative tasks of what users will do and you check to see if those rules of thumb are followed.
* This can be done by experts or designers and is a fast and easy way to evaluate an interface.
* This technique can fail to catch problems users might catch or identify if they were actually trying to use it themselves.

* Examples of heuristics
  * *Nielsen's heuristics*: simple and natural dialog, speak the user's language (do not use technical jargon), minimize the user's memory load, being consistent (within your application but also consistent with what users are used to interacting with), giving good feedback, providing clearly marked exits (if the users don't know what they want to do, they can get out), having shortcuts for expert users, preventing errors, giving good error messages and providing help and documentation.

3. Personas

* In this method, you come up with fictitious users representing a class of users.
* These personas then become a reference point for design and analysis. This prevents designers, programmers and other people who are thinking about an application from referring to themselves too much.
* Your persona has a goal or goals they want to accomplish, either in general or withing your system.

* Example of a Persona
  * Name: Frank
  * Goal: Wants encryption but in a simple, low-effort way
  * Overall goals: Wants easy to use email and social media tools that are encrypted to protect his privacy
  * Background: Undergraduate student, 21 years old, Psychology Major, Political activist, Savvy computer user but not an expert
  * About Frank: Frank is an undergraduate at the University of Maryland. He enjoys playing baseball, swimming and watching movies. He carries an iPhone and has a laptop and tablet. He is constantly connected and a frequent social media user. He is also a political activist and worries about his communications being monitored.

In conclusion, qualitative evaluation can provide insights into the usability of a system without measurements or timing. There are various levels of complexity (some of them, like heuristic evaluation can be pretty straightforward, but developing good personas can be something that can take hours to do and a team may spend a lot of time building the personas and doing the analysis). Also, some types of qualitative evaluation can be quick and inexpensive, but they may miss insights users provide.

## Running Controlled Experiments

The process of running controlled experiments

* We're using the scientific method, so we start out by stating a lucid, testable hypothesis.
* Then, we identify independent and dependent variables. That's what kind of things we're going to alter and what kind of things we're going to measure.
* We then design the experimental protocol. This is the actual steps of the experiment we're going to carry out in order to test our hypothesis.
* Then, we choose a user population. These are hopefully people who are going to use our system.
* Next stage is running some pilot participants. These can be anyone (friendly people?) willing to go through our experiment before we unleash it on the world.
* Based on the input from the pilot participants, we then fix our experimental protocol.
* Next step is running the experiment.
* Then we perform statistical analysis. This is going to let us know if we have real results that have meaning or if there's not a difference between the conditions that we tested.
* We then draw the conclusions.
* And finally, we communicate the results.

Experiment example

* The lucid, testable hypothesis: *Mobile phone login with fingerprint is faster than with PIN entry*.
* Choosing the variables: we manipulate one independent variable (the thing that we change) which is *the login method* and we observe the effect on one or more dependent variable (the thing that we measure) which is *the time it takes to login*.
* Designing the experimental protocol (the steps people go through when doing the experiment): in HCI, *we choose the tasks* first; we then need to decide whether we want to do a *between* (each subject runs one condition, e.g. half the people login with the PIN and half the people login with the password) or *within* (each subject runs several conditions, e.g. the same person would login both with the thumb print and with the PIN; these experiments tend to be more desirable but there can be some learning effects so we want to make sure our users are doing things in different order so they don't get better at tasks in one condition and then perform well later, when they do that same task under different conditions) subjects experiment.
* Running the experiment: after we run the pilot study, we should *have a checklist of steps* so all the users are doing the same things in the same order etc.; then we collect the data.
* Analysis: when we do a quantitative experiment it's *important we do a statistical comparison* (e.g. t-test).
* Once we have our analysis, we *report* our results.

## Usability Studies

In order to evaluate usability, we run a usability study to judge how an interface facilitates tasks with respect to the aspects of usability mentioned earlier: speed, efficiency, learnability, memorability and user preference.

When testing the usability of security, we should keep in mind that security is rarely the task users set out to accomplish and that good security is a seamless part of the task.

Usability Study Process
 
1. Define tasks (and their importance)
2. Develop Questionnaires (pre-test, post-test)
3. Evaluation
4. Reporting the results

1. Selecting Tasks

* Present it as a task, *not* as a question
  * Good - Create an itinerary with flights from BWI to Las Vegas departing December 30th and returning January 5th.
  * Bad - How many flights are available from BWI to Las Vegas departing December 30th and returning January 5th.
  * Because users are interested in planning an itinerary, not in counting them.
* Be specific!
  * Good - Find the calories, vitamins and minerals in a one 1c serving of broccoli.
  * Bad - Find nutrition information.
  * Because users shouldn't have to be creative to figure out what you want them to do.
* Don't give instructions
  * Good - Using google maps, find a street view of the Empire State Building.
  * Bad - Go to maps.google.com. In the search box, enter ...
  * Because you aren't testing anything if you give step by step instructions.
* Don't be vague or provide tiny insignificant tasks
  * Good - Using google maps, find a close up view that shows just the block with the Empire State Building.
  * Bad - Zoom in on a google map.
  * Because users don't come to the site to zoom, zooming is something that needs to be done as part of a real task.
* Choose representative tasks that reflect the most important things a user would do with the interface
  * Good - For Google, tasks would include a web search, a map search with directions, changing the language, conducting an advanced search (with the options specified) etc.
  * Bad - Do 5 basic web searches for different things.
  * Because repeated tasks do not provide new insights.
* Security Tasks
  * Security is almost never a task!
  * Good tasks for banking website:
    * Check balance
    * Make a transfer
  * Bad tasks for banking website:
    * Login to your account

2. Develop Questionnaires

* Pre-Test
  * Learn any relevant background about the subject: age, gender, education, experience ...
  * Perhaps more specific questions based on the site, e.g. color blindness, if the user has children etc.
* Post-Test
  * Have users provide feedback on the interface, e.g. Overall, I found this interface/website (difficult) 1 2 3 4 5 (very easy); Finding directions on a map was (frustrating) 1 2 3 4 5 (enjoyable)

3. Evaluation

* Happens once you've got the tasks and the questionnaires.
* The users are given the list of tasks, after completing the pre-test questionnaire, and they sit down with the system and just go through and do each of the tasks.
* Interaction with the user is governed by different (observation) protocols. The three main observation methods are
  * Silent Observer
  * Think Aloud
  * Constructive Interaction
* After you're done with the test, you administer your post-test questionnaire.
* Afterwards, it might be useful to do a short interview:
  * Ask users to give you feedback - it's easier for them than writing it down
  * Also, they will tell you things you never thought to ask

4. Reporting the results

* After the evaluation, report your results
* Summarize the experiences of users
* Emphasize your insights with specific examples or quotes
* Offer suggestions for improvement for tasks that were difficult to perform

Lessons

* *The Goal*: find out what part of a site or application are easy and hard to use.
* You can understand how usable is the site for each task.
* What improvements can be made to improve usability.
* For security - can you make it more seamless?

## A/B Testing

Relies on showing users two or more options and you put both of those options live on the web or live in your application and measure how well they perform.

Details on running an A/B test

* Start with a small percentage of visitors trying the experimental conditions.
* You want to do that so you can automatically stop testing if any condition has very bad performance.
* Finally, let people consistently see the same variation so they don't get confused (you can use Google Analytics for this).

Conclusions

* Small tweaks in the interface can lead to big differences in user behavior.
* A/B testing allows you to check that by showing different versions of the site to people.
* *You don't get any explanation about why that difference leads to the change in behavior* but it's still useful data to tweak your website and improve its performance.

## Additional Materials

* [You've been warned: an empirical study of the effectiveness of web browser phishing warnings] (http://repository.cmu.edu/cgi/viewcontent.cgi?article=1023&context=isr&sei-redir=1&referer=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3Dphishing%2Bwarnings%26btnG%3D%26as_sdt%3D1%252C21%26as_sdtp%3D#search=%22phishing%20warnings%22) by Egelman, Serge, Lorrie Faith Cranor, and Jason Hong, published in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pp. 1065-1074. ACM
* [How Obama Raised $60 Million by Running a Simple Experiment] (http://blog.optimizely.com/2010/11/29/how-obama-raised-60-million-by-running-a-simple-experiment/) by Siroker, Dan
* [Intro to Usability Testing] (https://designhammer.com/services/usability/introduction)


# Week 4

The whole lecture consists of explaining the material pointed to by this week's Additional Materials section.

## Additional Materials

* [Guidelines and strategies for secure interaction design] (http://sid.toolness.org/ch13yee.pdf) by Yee, Ka-Ping in Security and Usability: Designing Secure Systems That People Can Use (2005): 247-273


# Week 5

## Usable Authentication and Passwords

User preference, when it comes to passwords, is that they're easy to remember.

When people are asked to create passwords, they're first given a long set of rules (how long they should be: uppercase, lowercase etc.). If these rules are followed, the learnability and memorability of passwords will be harmed.

Additionally, many systems require you to change your password every six months.

Then, you're supposed to have different passwords for different systems.

The *solution*, from a usability perspective is to make passwords usable, not make people use password managers (or have alternative authentication schemes).

If you let people pick passwords that make sense to them, but require it in a way that keeps in mind the kind of attacks that can be used, you can create extremely secure passwords that are also extremely usable and easy for people to remember.

Also, having a system that implements time delays after each authentication (e.g. 5") and then increase that time after a number of failed attempts helps.

## Two Factor Authentication (TFA)

Consists of authenticating by means of a password + one time unique code. The unique code can be obtained in a number of ways: generated by a special purpose device (e.g. RSA SecurID), emailed to you by email, sent to you by text message, generated by an app (Google Authenticator).

TFA usability

  * Research says TFA is less usable than traditional, password-based, single-factor, authentication
    * Speed: slower
    * User preference: users felt it was less convenient, less usable and harder to use

Conclusion

  * TFA is *more secure but less usable* (so it's best use is for very sensitive systems that need highest security possible)

## Biometrics

A form of authentication that deals with using a person's biology to identify them. 

Relies on unique traits that can distinguish one person from another

  * Fingerprint
  * Scan of their eye
  * Facial recognition
  * Voice prints

Biometrics usability

  * Voice Recognition
    * Speed: medium
    * Efficiency: medium
    * Learnability: easy
    * Memorability: easy

  * Facial recognition
    * Speed: medium
    * Efficiency: medium
    * Learnability: easy
    * Memorability: easy

  * Fingerprint recognition
    * Speed: fast
    * Efficiency: good
    * Learnability: easy
    * Memorability: easy

When thinking about the security of various authentication systems that rely on biometrics we should ask the following questions

  * Who can access the device?
  * How easy they can they replicate the biometric input?

Conclusion

  * Biometrics are easy to use and relatively secure
  * Common on mobile devices but work anywhere
  * Compare usability

## Gesture-based Authentication

Can be related to biometric authentication but it doesn't have to be.

Types

  * Keypad gestures (e.g. connect the dots on Android)
  * Free gestures (e.g. draw something, multi-touch gestures etc.)

Benefits

  * Gestures users enjoy (easy, fun etc.) tend to be more secure
  * Users prefer gestures to passwords
  * Faster than passwords, less error prone

## Additional Materials

* [The Usability of Passwords] (https://www.baekdal.com/insights/password-security-usability) by Thomas Baekdal
* [5 Reasons We're Terrible at Choosing Passwords] (http://www.psychologytoday.com/blog/your-online-secrets/201410/5-reasons-were-terrible-choosing-passwords) by Jennifer Golbeck
* [Smudge Attacks on Smartphone Touch Screens] (https://www.usenix.org/legacy/event/woot10/tech/full_papers/Aviv.pdf) by Aviv, Adam J., et al. in WOOT 10 (2010): 1-7
* [XKCD Password Strength] (https://xkcd.com/936/)
* [Video: User-generated free-form gestures for authentication: security and memorability] (http://dl.acm.org/citation.cfm?id=2602429) by Michael Sherman et. al. 
* [Biometric-rich gestures: a novel approach to authentication on multi-touch devices] (http://dl.acm.org/citation.cfm?id=2208543) by Napa Sae-Bae et. al.
* [iSignOn signature authentication on the iPhone touch screen] (https://www.youtube.com/watch?v=cta7NJ4OLt8)
* [Password Portfolios and the Finite-Effort User: Sustainably Managing Large Numbers of Accounts] (https://research.microsoft.com/apps/pubs/default.aspx?id=217510) by Dinei Florencio et. al.


# Week 6

## Usable Privacy Basics

Privacy is a *kind* of security

  * Users want to protect their information
  * Users should understand what happens with their data
  * Users should have as much control as possible over how it's used

Privacy policies

  * These tell a user everything they need to know about how their data is collected, used and shared
  * Can be analyzed for usability (they should be clear, written in an accessible language, without too much technical or legal jargon and written with users in mind)
  * Case study: Facebook vs. Coursera vs. Twitter from a Privacy Policy point of view

Privacy controls

  * Should data be collected or not
  * Who has permission to see it
  * Case study: iPhone's Location Services controls (these allow one to control which apps have control to Location Services)

## Privacy Policy and User Understanding

For users to control their privacy, they must understand privacy policies. Do they (understand the privacy policies)?

What *we* know

  * Most people don't read privacy policies (about 16% of people say they read them all the time)
  * When people do read them, they don't necessarily understand them (half of people who say they've read a privacy policy say they know they don't understand what was in there)

How to learn

  * By reading privacy policies
  * Discover through other sources
  * Case study: a quick experiment on Facebook apps privacy policy
    * Ask people what data they think apps can access
    * Have them read privacy policy or watch a video (e.g. [Take This Lollipop] (http://www.takethislollipop.com/))
    * Ask again
    * Results
      * Every user underestimated what data could be accessed when they were first asked
      * After reading the privacy policy or watching the video, every user improved in their understanding of what data apps could access
      * The video led to greater improvements in user understanding
    * Implications
      * Privacy policies are boring and hard to read (and that means they have poor usability)
      * Privacy policies are important
      * Open question: Are there more usable ways to convey the information in a privacy policy?

## Informed Consent by Design

The section is based on the paper by Friedman et. al. in the Additional Materials section.

Informed consent exists as a concept outside of the space of privacy online but it applies there. It basically says that users understand what data is being collected and shared (i.e. they're informed) and that they consent to how it is being used.

The *informed consent* term is often used in research ethics.

The six components that are required for there to be informed consent in online privacy systems that the paper authors identified

  * Disclosure
  * Comprehension
  * Voluntariness
  * Competence
  * Agreement
  * Minimal distraction

Case studies presented

  * Gmail's informed consent with regard to its approach to content-triggered advertisements
  * Facebook's experiment (manipulating user's feeds)

Conclusions

  * Usable privacy requires informed consent from users
  * Users must understand how their data is being used and agree to it being used that way
  * The six components can help analyze a system for informed consent

## Five Pitfalls of Privacy

This section is based on the paper by Scott Lederer et. al. in the Additional Materials section.

The five pitfalls for designing for privacy can be broken into two categories

  * Understanding
    1. Obscuring potential information flow
    2. Obscuring actual information flow
  * Action
    3. Emphasizing configuration over action
    4. Lacking coarse-grained control
    5. Inhibiting established practice

Information flow talks about when people are sharing information, who is is shared with, what kind of information is it, who are the kind of observers, the media through which it is conveyed, the length of the retention of the information, the potential for unintended disclosure of the information, the collection of metadata and other things that fall into these categories.

Essentially the idea is that users are creating a lot of information and they should know what's done with it and where it's going after it's created.

1. Obscuring potential information flow

This basically means that there's a possible way information can be shared but it's not made clear to the user how that's actually going to happen.

Case study: Gmail's content-triggered advertisements made people concerned that the content of their messages were being shared with advertisers because it was unclear what Google was doing on Gmail.

2. Obscuring actual information flow

This means that information is being shared in a specific way, but that's being hidden from the users.

Case study: iPhone Privacy -> Location Services (scroll to the bottom) -> System Services -> Frequent Locations. This is a list of places iPhone users go frequently and is compiled automatically (i.e. privacy isn't being controlled by the user).

3. Emphasizing configuration over action

This is something that happens when privacy management gets all caught up in privacy tools and users have to control lots of settings instead of privacy being just a natural part of workflow.

The papers suggests that privacy management should be integrated into the natural workflow of users so that they don't have to think about it. Same guideline is valid for security.

4. Lacking coarse-grained controls

Refers to the need for a high-level, obvious control which allows one to turn sharing on and off.

This can be easily imagined like an airplane mode, but for privacy.

Case study: Amazon's lack of a control that allows you to turn off the system that keeps track of what you look at. An example of how this might actually help the system make better recommendations is when you're trying to find a present for somebody else but you're not actually interested in the object of interest.

5. Inhibiting established practice

This means that we want to ask what users expect from other experiences and we want to let them expect that here too. Think of mental models, conventions etc.

Conclusions

  * Make it clear to users how information is being shared
  * Make it easy and natural for users to control privacy
  * Make the default practice match users' expectations

## Inferring Personal Data

This section consists in its entirety on the TED talk listed in the Additional Materials section.

## Additional Materials

  * [Informed consent by design] (http://hornbeam.cs.ucl.ac.uk/hcs/teaching/GA10/lec9extra/ch24friedman.pdf) by Batya Friedman, Peyina Lin, and Jessica K. Miller in Security and Usability (2005): 495-521
  * [Personal privacy through understanding and action: five pitfalls for designers] (http://repository.cmu.edu/cgi/viewcontent.cgi?article=1077&context=hcii&sei-redir=1) by Scott Lederer et al. in Personal and Ubiquitous Computing 8.6 (2004): 440-454
  * [The curly fry conundrum: Why social media “likes” say more than you might think] (https://www.ted.com/talks/jennifer_golbeck_the_curly_fry_conundrum_why_social_media_likes_say_more_than_you_might_think), TED talk by Jennifer Golbeck
  * [Why we overshare online] (http://www.psychologytoday.com/blog/your-online-secrets/201410/why-we-overshare-online) by Jennifer Golbeck