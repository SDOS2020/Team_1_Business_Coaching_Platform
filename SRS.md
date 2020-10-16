<center> 
    <h1> Business Coaching </h1>
    <h2> Software Requirements Specification </h2>
</center>
<br>
<h2> Table Of Contents </h2>

1. ### Introduction
    1. Purpose
    1. Scope
    1. Overview
    1. Glossary
    1. References
1. ### Specific Requirements
    1. Functionality
    1. Home Page
    1. Signup
    1. Login Page
    1. Dashboard
    1. Profile Page
    1. Requesting Sessions for New clients
    1. Book a Free Session for New clients
    1. Enrolment for New clients
    1. Dedicated Page for Coach-client
    1. Time-bound Action Plan
    1. Chat-Box
    1. Sharing Resources
    1. Calendar Integration
    1. Note-taking
    1. Payment Gateway
    1. Event Reminders
    1. Track Milestones
    1. Linking Psychometric Assessment Portal
    1. Events
    1. Performance	
    1. Security	
    1. Design Constraints	
    1. Interface
1. ### Supporting Information
    1. Use-Case Diagram
    1. Architecture Diagram

## Introduction
1. ### Purpose
    Business Coaching is becoming increasingly important for shifting focus to the individual and investing in the person to develop his/her overall skills in the corporate world. A coach helps us see clearly where we are today, and helps us find ways to move forward to fulfil our goals. The goal of our project is to build a platform dedicated to business coaches. We aim to enhance the experience of personalised online coaching by creating software that adheres to the needs of both the coach and coachee.
    In this document, we analyse and provide an in-depth insight into our software for business coaches. We comment upon the project’s target audience and enlist its hardware and software requirements. We define the various capabilities and features required by the stakeholders of the project.
1. ### Scope
    The scope of our project is limited to independent business coaches and people who seek business coaching, i.e, the coachees. A coachee would be able to avail the benefits of the platform after registering and enrolling for a package with a preferred coach. We aim to focus on the needs of our stakeholders and the potential users of our portal.

1. ### Overview
    The remaining sections of the document lay emphasis on the characteristics of the project, functional and data requirements of the product. Section 2 enlists functional requirements, the constraints and assumptions made while designing the platform. Section 3 includes supporting information. 




1. ### Glossary

    Term | Definition
    ------------ | -------------
    Coach | A person who is responsible for helping a coachee realise his/her goals through one on one sessions and customized tasks
    Coachee | A person who seeks help to realise his/her goals and performs assigned tasks by the coach
    User | A coach or coachee using the platform
    Mind Map | An illustration of information with a central idea placed in the middle and associated ideas arranged around it
    Milestone | A significant long-term accomplishment for the coachee, achieved by completion of a certain number of actions
    Action Plan | A weekly list of actions/tasks suggested by the coach that a coachee needs to follow
    Chat Box | A window for instant communication between coach and coachee
    Psychometric Assessment | An objective way to measure the potential ability of candidates to perform well in a job role
    Connection | For a coachee, all coaches with whom he/she has enrolled. For a coach, all coachees enrolled with him/her 
    Dedicated Page | A page for each coach-coachee coaching experience.

5. ### References
    1. [SRS Sample Document](https://www.utdallas.edu/~chung/RE/Presentations07S/Team_1_Doc/Documents/SRS4.0.doc)

<br>

## Specific Requirements
1. ### Functionality
    1. #### Home Page
        1. The system shall display a grid view of some coaches with maximum testimonials in the home page.
        1. The system shall display information about business coaching.
        1. The system shall display information about business coaching.
        1. The system shall enable a user to go to the online psychometric assessment portal.
        1. The system shall enable a user to sign up for our service.
        1. The system shall enable existing users to login.
        1. The system shall provide access to free resources for coaches and clients.
        1. The system shall provide information about complimentary events being conducted by coaches registered with the portal.
    1. #### Signup
        1. As Coach
            1. The system shall ask for name, email, payment details, location, experience, area of expertise, social media profiles, bio and profile photo for sign up.
            1. The system shall successfully register a coach only after the authentication is complete.
            1. The system shall allow the administrator to authenticate the coach.
        1. As client
            1. The system shall ask for only name and email for registration.
            1. The system shall allow a client to fill additional details like location, resume, social media profiles, reasons for seeking coaching, contact info after sign up.
    1. #### Login Page
        1. The system shall allow registered users to login through their email and password.
        1. The system shall allow users to reset their password using their registered email id.
    1. #### Dashboard
        1. As Coach
            1. The system shall provide a coach with a calendar which will have links to all scheduled video calls and upcoming event details.
            1. The system shall provide a coach with a list of the sessions scheduled for today.
            1. The system shall provide a coach with a chatbox.
            1. The system shall provide a list view of profiles of all clients who request to book a free session with the coach.
            1. The system shall provide 2 options to the coach
                1. Accept
                1. Decline
            1. The system shall book a slot in the calendar for the session.
            1. The system shall provide a list view of profiles of all clients who request to enrol with the coach.
            1. The system shall provide 2 options to the coach
                1. Accept
                1. Decline
            1. The system shall create a dedicated page for coach-client if the coach accepts the request.
            1. The system shall provide a list of current clients hyperlinked to their dedicated page.
            1. The system shall archive past clients who enrolled with the coach.
            1. The system shall enable a coach to view his/her profile page.
            1. The system shall allow a coach to add information about his/her events.
        1. As Client
            1. The system shall provide a client with a calendar which will have links to all scheduled video calls and upcoming event details.
            1. The system shall provide a client with today's action plan.
            1. The system shall provide a client with a chat box.
            1. The system shall provide a list of current coaches hyperlinked to their dedicated page.
            1. The system shall direct a client to an enrolment page to book free sessions and enrol under different coaches.
            1. The system shall enable a client to view his/her profile page.
    1. #### Profile Page
        1. As Coach
            1. The system shall provide the following information:
                1. _Name_
                1. _Title_
                1. _Work-Experience_
                1. _Bio_
                1. _Testimonials by past clients_
                1. _Links to social media profiles_
            1. The system shall allow the coach's profile to be viewed by everyone.
            1. The system shall allow users to add testimonials for the coach.
        1. As Client
        1. The System shall provide the following information:
            1. _Name_
            1. _Email_
            1. _Links to social media profiles_
        1. The system shall allow the client's profile to be viewed only by his/her connections. 
    1. #### Requesting Sessions for New Clients
        1. The system shall provide a search bar to search for different coaches.
        1. The system shall enable a user to filter their searches in search bar by area of expertise. 
        1. The system shall provide a grid view of coaches which are hyperlinked to their profiles.
        1. The system shall show coach's name in the grid view
        1. The system shall show coach's profile photo in the grid view
        1. The system shall show coach's area of expertise in the grid view
        1. The system shall show coach's bio in the grid view
        1. The system shall show available appointment slots with the coach for the next month
        1. The system shall allow a client make the following requests-
            1. Book a free session
            1. Enroll for desired number of sessions 
        1. The system shall allow a client to make a request if he/she has filled the entire profile, including additional details
    1. #### Book a Free Session for New Clients
        1. The system shall allow a client to book a free session with the desired coach. 
        1. The system shall allow client to choose a slot from the available 1 month slots of the coach and send a request. 
        1. The system shall allow coaches to accept or deny session requests.
        1. The system shall book the slot in the calendar for both coach and client if the request is accepted by the coach. 
        1. The system shall add video conferencing details in the slot booked for the session. 
    1. #### Enrolment for New Clients
        1. The system shall allow client to enrol with a coach for a desirable number of sessions 
        1. The system shall allow client to request for an enrolment with the coach
        1. The system shall allow coach to accept or deny enrolment requests
        1. The system shall direct client to the payment gateway if the request is accepted by the coach.
        1. The system shall create a dedicated coach-client page upon successful payment by the client. 
    1. #### Dedicated Page for Coach-Client
        1. The system shall display resources posted to the user such as 
            1. Mind Maps
            1. Notes
        1. The system shall display a calendar for the current coaching plan. 
        1. The system shall display a chatbox for coach-client interaction via text.
        1. The system shall display a roadmap for the client with long-term milestones. 
        1. The system shall display an extend program tab for the client which will direct to the payment gateway.
        1. The system shall display a time-bound action plan for the client.
        1. The system shall display announcements posted by the user.
        1. The system shall display number of sessions remaining between coach and client
    1. #### Time-bound Action Plan
        1. The system shall allow user to schedule weekly actions/tasks for the client
        1. The system shall allow user to add task description
        1. The system shall allow client to mark a task/action as completed before the due date
        1. The system shall allow user to edit and delete scheduled actions
        1. The system shall mark the action as overdue if not completed within the specified time.
    1. #### Chat-Box
        1. The system shall allow a user to send messages less than 1000 characters to his/her connections
    1. #### Sharing Resources
        1. The system shall allow a user to post announcements (text) to their dedicated page.
        1. The system shall allow a user to post files less than 25 Mb to their dedicated page.
    1. #### Calendar Integration
        1. The system shall provide a calendar for all users.
        1. The system shall allow a coach to schedule events with a client based on their calendar.
        1. The system shall enable a user to look at upcoming events on his/her calendar.
    1. #### Note-taking
        1. The system shall allow a user to take notes along with video conferencing.
        1. The system shall allow a user to post notes in the resources section.
        1. The system shall provide a dedicated page for a user to take individual notes
    1. #### Building Mind-Map
        1. The system shall provide a drawing board with view and edit access to the coach
        1. The system shall have a drag and drop functionality to create text boxes
        1. The system shall allow user to add branches to text-boxes
        1. The system shall allow user to add text above branches
        1. The system shall allow user to add branches to existing branches
    1. #### Payment Gateway
        1. The system shall allow a client to enrol for the desired number of sessions
        1. The system shall allow a client to make domestic payments via online banking or credit/debit cards
    1. #### Event Reminders
        1. The system shall allow a user to set the frequency of receiving reminders/notifications via email.
        1. The system shall provide reminders to client for upcoming sessions and task deadlines.
        1. The system shall provide reminders to coach for upcoming sessions.
        1. The system shall notify the coach in case of a new appointment request
        1. The system shall notify the client in case of a new session invite and when a new task is assigned
    1. #### Track Milestones
        1. The system shall allow coach to set milestones (long term task) for client
        1. The system shall allow the coach to mark a milestone as completed when a client successfully performs corresponding tasks/actions assigned

    1. #### Linking Psychometric Assessment Portal
        1. The system shall provide access to an online psychometric assessment service.
        1. The system shall provide access to the assessment report generated to both coach and client.
    1. #### Events
        1. The system shall allow a coach to add information about seminars/talks being conducted by him/her.

1. ###  Performance
    1. The product shall be based on the web and has to be run from a web server.
    1. The product shall take initial load time depending on internet connection strength which also depends on the media from which the product is run.
    1. The performance shall depend upon hardware components of the user.

1. ### Security
    1. The user’s web browser shall never display a customer’s password in plain text.
    1. The system’s back-end servers shall only be accessible to authenticated administrators.
    1. The system shall store hash of all passwords in the database using a one-way function.
    1. The system shall not allow a client to view his/her coaches' connections.
    1. The system shall provide a secure payment gateway through RazorPay.

1. ### Design Constraints	
    1. Web-Based Product
        1. There are no memory requirements
        1. The computers must be equipped with a web browser such as Google Chrome, Firefox, etc.
        1. The computer shall be enabled with a microphone and a webcam
    1. Cloud Requirements
        1. The system shall be hosted on a cloud platform

1. ### Interfaces 
    1. User Interfaces
        1. The user interface for the software shall be compatible with any browser such as Internet Explorer, Mozilla, Google Chrome by which user can access the system.
    1. Hardware Interfaces
        1. The system shall require to connect to the internet. Hardware required would be WAN, Ethernet Cable etc.
## Supporting Information
1. ### Use-Case Diagram
    ![Alt text](https://github.com/SDOS2020/Team_1_Business_Coaching_Platform/blob/main/Images/UseCase.jpg?raw=true "Use-Case")
2. ### Architecture Diagram
    ![Alt text](https://github.com/SDOS2020/Team_1_Business_Coaching_Platform/blob/main/Images/Architecture.jpeg?raw=true "Use-Case")