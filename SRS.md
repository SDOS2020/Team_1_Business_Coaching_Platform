

**Business Coaching**

**Software Requirements Specification**

**SDOS Group-1**

Anmol Singhal (2017332)

Shreyansh Nagpal (2017109)

Tejas Oberoi (2017367)

Yatin Kumar Arora (2017124)





**Table of Contents**

1.**Introduction**

**3**

3

3

3

3

4

1.1.

1.2.

1.3.

1.4.

1.5.

Purpose

Scope

Overview

Glossary

References

2.**Specific Requirements**

**4**

5

2.1.1.

2.1.2.

Functionality

Home Page

5

2.1.3.

Signup

5

2.1.4.

Login Page

5

2.1.5.

Dashboard

5

2.1.6.

Profile Page

6

2.1.7.

Requesting Sessions for New clients

Book a Free Session for New clients

Enrolment for New clients

Dedicated Page for Coach-client

Time-bound Action Plan

Chat-Box

7

2.1.8.

7

2.1.9.

7

2.1.10.

2.1.11.

2.1.12.

2.1.13.

2.1.14.

2.1.15.

2.1.16.

2.1.17.

2.1.18.

2.1.19.

2.1.20.

8

8

8

Sharing Resources

Calendar Integration

Note-taking

8

8

9

Payment Gateway

Event Reminders

9

9

Track Milestones

9

Linking Psychometric Assessment Portal

Events

9

10

10

10

10

10

2.2.

2.3.

2.4.

2.5.

Performance

Security

Design Constraints

Interfaces

3.**Supporting Information**

3.1. Use-Case Diagram

**11**

12

2





**1. Introduction**

**1.1.**

**Purpose**

Business Coaching is becoming increasingly important for shifting focus to the

individual and investing in the person to develop his/her overall skills in the

corporate world. A coach helps us see clearly where we are today, and helps us

find ways to move forward to fulfil our goals. The goal of our project is to build a

platform dedicated to business coaches. We aim to enhance the experience of

personalised online coaching by creating software that adheres to the needs of

both the coach and client.

In this document, we analyse and provide an in-depth insight into our software for

business coaches. We comment upon the project’s target audience and enlist its

hardware and software requirements. We define the various capabilities and

features required by the stakeholders of the project.

**1.2.**

**Scope**

The scope of our project is limited to independent business coaches and people

who seek business coaching, i.e, the clients. A client would be able to avail the

benefits of the platform after registering and enrolling for a package with a

preferred coach. We aim to focus on the needs of our stakeholders and the

potential users of our portal.

**1.3.**

**Overview**

The remaining sections of the document lay emphasis on the characteristics of

the project, functional and data requirements of the product. Section 2 enlists

functional requirements, the constraints and assumptions made while designing

the platform. Section 3 includes supporting information.

3





**1.4.**

**Glossary**

**Term**

**Definition**

Coach

Client

User

A person who is responsible for helping a client realise his/her goals

through one on one sessions and customized tasks

A person who seeks help to realise his/her goals and performs

assigned tasks by the coach

A coach or client using the platform

Mind Map

Milestone

Action Plan

Chat Box

An illustration of information with a central idea placed in the middle

and associated ideas arranged around it

A significant long-term accomplishment for the client, achieved by

completion of a certain number of actions

A weekly list of actions/tasks suggested by the coach that a client

needs to follow

A window for instant communication between coach and client

Psychometric

Assessment

An objective way to measure the potential ability of candidates to

perform well in a job role

Connection

For a client, all coaches with whom he/she has enrolled

For a coach, all clients enrolled with him/her

Dedicated Page

A page for each coach-client coaching experience.

**1.5.**

**References**

\1. [SRS](https://www.utdallas.edu/~chung/RE/Presentations07S/Team_1_Doc/Documents/SRS4.0.doc)[ ](https://www.utdallas.edu/~chung/RE/Presentations07S/Team_1_Doc/Documents/SRS4.0.doc)[Sample](https://www.utdallas.edu/~chung/RE/Presentations07S/Team_1_Doc/Documents/SRS4.0.doc)[ ](https://www.utdallas.edu/~chung/RE/Presentations07S/Team_1_Doc/Documents/SRS4.0.doc)[Document](https://www.utdallas.edu/~chung/RE/Presentations07S/Team_1_Doc/Documents/SRS4.0.doc)

4





**2. Specific Requirements**

**2.1.**

**Functionality**

**2.1.1. Home Page**

A. The system shall display a grid view of some coaches with maximum

testimonials in the home page

B. The system shall display information about business coaching.

C. The system shall enable a user to go to the online psychometric

assessment portal.

D. The system shall enable a user to sign up for our service.

E. The system shall enable existing users to login.

F. The system shall provide access to free resources for coaches and

clients.

G. The system shall provide information about complimentary events being

conducted by coaches registered with the portal.

**2.1.2.**

**Signup**

A. As Coach

a. The system shall ask for name, email, payment details, location,

experience, area of expertise, social media profiles, bio and profile

photo for sign up.

b. The system shall successfully register a coach only after the

authentication is complete.

c. The system shall allow the administrator to authenticate the

coach.

B. As client

a. The system shall ask for only name and email for registration.

b. The system shall allow a client to fill additional details like

location, resume, social media profiles, reasons for seeking

coaching, contact info after sign up.

**2.1.3.**

**2.1.4.**

**Login Page**

A. The system shall allow registered users to login through their email and

password.

B. The system shall allow users to reset their password using their

registered email id.

**Dashboard**

A. As Coach

5





a. The system shall provide a coach with a calendar which will have

links to all scheduled video calls and upcoming event details.

b. The system shall provide a coach with a list of the sessions

scheduled for today.

c. The system shall provide a coach with a chatbox.

d. The system shall provide a list view of profiles of all clients who

request to book a free session with the coach.

i.

The system shall provide 2 options to the coach

\1. Accept

\2. Decline

ii.

The system shall book a slot in the calendar for the

session.

e. The system shall provide a list view of profiles of all clients who

request to enrol with the coach.

i.

The system shall provide 2 options to the coach

\1. Accept

\2. Decline

ii.

The system shall create a dedicated page for coach-client

if the coach accepts the request.

f. The system shall provide a list of current clients hyperlinked to

their dedicated page.

g. The system shall archive past clients who enrolled with the coach.

h. The system shall enable a coach to view his/her profile page.

i. The system shall allow a coach to add information about his/her

events.

B. As Client

a. The system shall provide a client with a calendar which will have

links to all scheduled video calls and upcoming event details.

b. The system shall provide a client with today's action plan.

c. The system shall provide a client with a chat box.

d. The system shall provide a list of current coaches hyperlinked to

their dedicated page.

e. The system shall direct a client to an enrolment page to book free

sessions and enrol under different coaches.

f. The system shall enable a client to view his/her profile page.

**2.1.5.**

**Profile Page**

A. As Coach

a. The system shall provide the following information:

i.

ii.

Name

Title

iii.

iv.

v.

Work-Experience

Bio

Testimonials by past clients

6





vi.

Links to social media profiles

b. The system shall allow the coach's profile to be viewed by

everyone.

c. The system shall allow users to add testimonials for the coach.

B. As Client

a. The System shall provide the following information:

i.

ii.

Name

Email

iii.

Links to social media profiles

b. The system shall allow the client's profile to be viewed only by

his/her connections.

**2.1.6.**

**Requesting Sessions for New Clients**

A. The system shall provide a search bar to search for different coaches.

B. The system shall enable a user to filter their searches in search bar by

area of expertise.

C. The system shall provide a grid view of coaches which are hyperlinked to

their profiles.

a. The system shall show coach's name in the grid view

b. The system shall show coach's profile photo in the grid view

c. The system shall show coach's area of expertise in the grid view

d. The system shall show coach's bio in the grid view

e. The system shall show available appointment slots with the coach

for the next month

D. The system shall allow a client make the following requests-

a. Book a free session

b. Enroll for desired number of sessions

E. The system shall allow a client to make a request if he/she has filled the

entire profile, including additional details

**2.1.7.**

**Book a Free Session for New Clients**

A. The system shall allow a client to book a free session with the desired

coach.

B. The system shall allow client to choose a slot from the available 1 month

slots of the coach and send a request.

C. The system shall allow coaches to accept or deny session requests.

D. The system shall book the slot in the calendar for both coach and client if

the request is accepted by the coach.

E. The system shall add video conferencing details in the slot booked for the

session.

**2.1.8.**

**Enrolment for New Clients**

A. The system shall allow client to enrol with a coach for a desirable number

of sessions

7





B. The system shall allow client to request for an enrolment with the coach

C. The system shall allow coach to accept or deny enrolment requests

D. The system shall direct client to the payment gateway if the request is

accepted by the coach.

E. The system shall create a dedicated coach-client page upon successful

payment by the client.

**2.1.9.**

**Dedicated Page for Coach-Client**

A. The system shall display resources posted to the user such as

a. Mind Maps

b. Notes

B. The system shall display a calendar for the current coaching plan.

C. The system shall display a chatbox for coach-client interaction via text.

D. The system shall display a roadmap for the client with long-term

milestones.

E. The system shall display an extend program tab for the client which will

direct to the payment gateway.

F. The system shall display a time-bound action plan for the client.

G. The system shall display announcements posted by the user.

H. The system shall display number of sessions remaining between coach

and client

**2.1.10.**

**Time-bound Action Plan**

A. The system shall allow user to schedule weekly actions/tasks for the

client

B. The system shall allow user to add task description

C. The system shall allow client to mark a task/action as completed before

the due date

D. The system shall allow user to edit and delete scheduled actions

E. The system shall mark the action as overdue if not completed within the

specified time.

**2.1.11.**

**2.1.12.**

**Chat-Box**

A. The system shall allow a user to send messages less than 1000

characters to his/her connections

**Sharing Resources**

A. The system shall allow a user to post announcements (text) to their

dedicated page.

B. The system shall allow a user to post files less than 25 Mb to their

dedicated page.

**2.1.13.**

**Calendar Integration**

A. The system shall provide a calendar for all users.

8





B. The system shall allow a coach to schedule events with a client based on

their calendar.

C. The system shall enable a user to look at upcoming events on his/her

calendar.

**2.1.14.**

**2.1.15.**

**Note-taking**

A. The system shall allow a user to take notes along with video

conferencing.

B. The system shall allow a user to post notes in the resources section.

C. The system shall provide a dedicated page for a user to take individual

notes

**Building Mind-Map**

A. The system shall provide a drawing board with view and edit access to

the coach

B. The system shall have a drag and drop functionality to create text boxes

C. The system shall allow user to add branches to text-boxes

D. The system shall allow user to add text above branches

E. The system shall allow user to add branches to existing branches

**2.1.16.**

**2.1.17.**

**Payment Gateway**

A. The system shall allow a client to enrol for the desired number of

sessions

B. The system shall allow a client to make domestic payments via online

banking or credit/debit cards

**Event Reminders**

A. The system shall allow a user to set the frequency of receiving

reminders/notifications via email.

B. The system shall provide reminders to client for upcoming sessions and

task deadlines.

C. The system shall provide reminders to coach for upcoming sessions.

D. The system shall notify the coach in case of a new appointment request

E. The system shall notify the client in case of a new session invite and

when a new task is assigned

**2.1.18.**

**Track Milestones**

A. The system shall allow coach to set milestones (long term task) for client

B. The system shall allow the coach to mark a milestone as completed when

a client successfully performs corresponding tasks/actions assigned

9





**2.1.19.**

**2.1.20.**

**Linking Psychometric Assessment Portal**

A. The system shall provide access to an online psychometric assessment

service.

B. The system shall provide access to the assessment report generated to

both coach and client.

**Events**

A. The system shall allow a coach to add information about seminars/talks

being conducted by him/her.

**2.2.**

**Performance**

A. The product shall be based on the web and has to be run from a web server.

B. The product shall take initial load time depending on internet connection strength

which also depends on the media from which the product is run.

C. The performance shall depend upon hardware components of the user.

**2.3.**

**Security**

A. The user’s web browser shall never display a customer’s password in plain text.

B. The system’s back-end servers shall only be accessible to authenticated

administrators.

C. The system shall store hash of all passwords in the database using a one-way

function.

D. The system shall not allow a client to view his/her coaches' connections.

E. The system shall provide a secure payment gateway through RazorPay.

**2.4.**

**Design Constraints**

A. *Web-Based Product*

a. There are no memory requirements

b. The computers must be equipped with a web browser such as Google

Chrome, Firefox, etc.

c. The computer shall be enabled with a microphone and a webcam

B. Cloud Requirements

a. The system shall be hosted on a cloud platform

10





**2.5.**

**Interfaces**

A. User Interfaces

a. The user interface for the software shall be compatible with any browser

such as Internet Explorer, Mozilla, Google Chrome by which user can

access the system.

B. Hardware Interfaces

a. The system shall require to connect to the internet. Hardware required

would be WAN, Ethernet Cable etc.

11





**3. Supporting Information**

**3.1.**

**Use-Case Diagram**

12

