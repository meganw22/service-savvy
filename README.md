# Service Savvy
![image](https://github.com/meganw22/service-savvy/assets/141934888/947d872d-e299-46ed-a61f-ec50414cb99a)


## Introduction

Service savvy is a centralised platform for communication between users and maintenance staff. This service enables users to articulate their maintenance needs quickly and accurately to support smoother operations within the workplace. This platform is user friendly, with a simple design and effective tracking and feedback capabilities for both the users and maintenance team. 

## User Stories
- As a user, I want to be able to create a new maintenance item, providing essential details about the issue.
- As a user, I want to have a dedicated profile page for myself where I can view and manage my profile and keep the information private from general view.
- As a user, I want to see a user-friendly homepage which provides relevant information and navigation options.
- As a user, I want to log in and out of my account securely. 
- As a user, I want to edit, update, and delete my tickets after initial creation to provide additional information or make corrections if necessary.
- As a user, I want to be able to sort the tickets based on different criteria, such as date, urgency, or status.
- As a user, I want to be able to leave comments on tickets for feedback and follow up purposes.
- As a user, I want to be able to close tickets and mark them as completed for better t tracking and performance purposes.
- As an admin, I want only authenticated users to have access to ticket CRUD functionality.

## Entity Relationship Diagrams (ERD)
| Entity         | Attributes                 |
|----------------|----------------------------|
| User           | username: CharField     | 
|                | user_type: IntegerField  |
| Ticket         | title: CharField         | 
|                | slug: SlugField          |
|                | username: ForeignKey(User) | 
|                | Job Category: IntegerField |
|                | Job Description: CharField |
|                | Created_on: DateTimeField |
|                | Location: CharField      |
|                | Priority: IntegerField   |
|                | is_complete: BooleanField |
|                | completed_by: ForeignKey(User) |
|                | completed_at: DateTimeField |
|                | update_on: DateTimeField |
| About          | User: OneToOneField(User) |
|                | title: CharField        | 
|                | update_on: DateTimeField |
|                | job_title: TextField |
|                | email: CharField |
|                | tel: CharField |
|                | memeber_since: DateTimeField |
| Comment        | ticket: ForeignKey(Ticket) |
|                | username: ForeignKey(User) | 
|                | body: TextField |
|                | Created_on: DateTimeField |


 

## Wireframes

![homepage drawio](https://github.com/meganw22/service-savvy/assets/141934888/5b25dc16-9bb7-410c-80c1-6f46753929e7)

![ticket list drawio](https://github.com/meganw22/service-savvy/assets/141934888/44da37d1-e83b-4fc6-928c-2b2b322a6f90)

![ticket detail drawio](https://github.com/meganw22/service-savvy/assets/141934888/10db718f-4a60-4153-aa27-d45db74cc61d)

![create ticket drawio](https://github.com/meganw22/service-savvy/assets/141934888/547e8c76-3d35-48e9-907c-aaeda5a86756)

![update ticket drawio](https://github.com/meganw22/service-savvy/assets/141934888/c71b40ff-9ce0-4e60-8e32-9a46bb2857ce)

## Features
Service savvy is fully responsive and easy for new users to navigate. It required users to be authenticated when viewing and amending details but the homepage is available for all users to view.

### Nav Bar
The nav bar includes the logo, and nav links for Home, Tickets and User Profile page.
Unauthenticated view of nav bar:
![image](https://github.com/meganw22/service-savvy/assets/141934888/fd551651-c953-41d1-88df-97f0dc9a43f2)

Authenticated view of nav bar:
![image](https://github.com/meganw22/service-savvy/assets/141934888/90b1d7e2-dd6a-4edc-bbb0-4c4c75250eef)

### Footer
the footer is consistent throughout the webpages and is responsive:
![image](https://github.com/meganw22/service-savvy/assets/141934888/4a5a2a15-7855-4a56-afef-ac911d30ee42)

## Homepage
The homepage displays a simple structure, welcoming users to the portal. It contains hyperlinks to prompt the user into creating or logging in to an account before they are able to view the rest of the website content. 
Further down the homepage, there is a section containing emergency information for a user to contact. It is displayed in obvious and large formatting.

Unauthenticated display

![image](https://github.com/meganw22/service-savvy/assets/141934888/6182be73-72ab-47dc-90c0-10ad92c03de2)

Authenticated display

![image](https://github.com/meganw22/service-savvy/assets/141934888/ab97e897-4e22-4780-9455-0a22a54bb5fc)

### Register
The user is directed to registration form which is provided by Django. It allows a user to create an account with prompts and suggestion for a secure password. 

![image](https://github.com/meganw22/service-savvy/assets/141934888/4a21c23d-0bf5-4ba1-b283-3aaafe78df4a)

### Login
The Login view is provided by Django and allows the user to log into their account. With this, the user will now have authentication and will be able to see more aspects of the website that were limited to them before. The user is shown a successful log in alert at the top of the page.

![image](https://github.com/meganw22/service-savvy/assets/141934888/af6956d1-e5fe-492d-8005-aaddcb3a6b32)

### Sign out
The sign out view is a 2 step process to confirm the user wants to log out. The user is redirected to the homepage and is shown a successful 'log out' alert at the top of the screen.

![image](https://github.com/meganw22/service-savvy/assets/141934888/bde942f0-d615-476c-9091-2e08b55cad55)

## Tickets 
Within the maintenance portal, a ticket raised means a problem has occurred. The user creating the ticket will fill in the details and submit it, sending it to the ticket list view. All authenticated user can see all tickets. 

### List
The ticket list, shows all created tickets raised by users. The tickets are sorted, by default, in order of highest priority first with a secondary filter, oldest created. This is useful for maintenance members who want a quick view of which tickets are the higher priority tickets and what needs addressing first.

![image](https://github.com/meganw22/service-savvy/assets/141934888/8660f842-22b0-4301-8972-b39f99984925)

The sort filter dropdown has multiple options allowing flexible view of tickets. The tickets listed are all incomplete tickets and are awaiting fixing. All completed tickets are separated through another filter called 'Completed'
Users also have the option of displaying only their own tickets which is very useful to navigate in the future when the website is increasingly used and there could be 100's of tickets raised.

![image](https://github.com/meganw22/service-savvy/assets/141934888/bf4b065f-64a3-4bfd-a6f6-2a25559b2177)

### Create Tickets
The ticket creation form provides a template for the user to populate with details of their problem.
Fields include:
- Title
- Job Category, with dropdown options
- Job description
- Location
- Priority, with dropdown options

![image](https://github.com/meganw22/service-savvy/assets/141934888/273e7499-e32f-43de-be83-2a742715ef8b)

### Ticket Details View
The ticket detail view is displayed when a user opens a created ticket. It provides the details of the ticket and has some targeted authentication rules that only the user raising the ticket can see.

![image](https://github.com/meganw22/service-savvy/assets/141934888/2ce2c561-9503-41d7-b80b-346718ae1251)

If a user is not the creator of a ticket they cannot edit, delete or complete the ticket.

![image](https://github.com/meganw22/service-savvy/assets/141934888/fc063f2f-0a07-4ec1-b138-6673a1cf8836)

### Update Tickets
Only the authenticated user who created the ticket, can update the ticket. For all other users, the update button is not displayed or available.
The update view will display the pre-populated values of the current ticket and will allow the user to make adjustments and save changes. 
When updates are saved, Users can see the new 'Last Updated On' time stamp differ from the 'Created on' timestamp. 

### Comments
Underneath the ticket detail, Users are able to leave comments. These comments can be viewed by any authenticated user and is the primary method of communication between the ticket creator and the maintenance team.
![image](https://github.com/meganw22/service-savvy/assets/141934888/532f5157-3b69-45c4-9a80-35b2d065ab76)

#### Creating comments
Any user can leave a comment and each user comment is posted with a Username and timestamp attached. 

#### Deleting comments
Users can only delete their own tickets and cannot delete other users tickets.
![image](https://github.com/meganw22/service-savvy/assets/141934888/d8c07fc3-34fc-4ef3-9056-24713d613111)

### Delete
Only the authenticated user who created the ticket, can delete the ticket. For all other users, the delete button is not displayed or available.
The delete ticket process is a 2-step verification where the user is directed to a new page to confirm ticket requires deleting before they are re-directed back to the tickets list page.
![image](https://github.com/meganw22/service-savvy/assets/141934888/bb836727-84d9-4f16-843d-ee8d0ad8a69a)

### Profile details 
When a user is authenticated they can navigate to their about page to populate and manage their own details.
![image](https://github.com/meganw22/service-savvy/assets/141934888/57412db8-effc-4cba-bc64-ee0c1d322b53)


# Future Implementation
## Utilise the Archive model
Creating an Archive model can be beneficial for data organisation, performance and user experience. I have implemented a form of separation of completed tickets from incomplete tickets but and archive feature can keep the database more organised and easier to manage. For performance purposes, a separate database to hold the completed data would benefit the performance greatly by reducing the size of the active ticket database. Finally, user experience will improve as the new model will de-clutter the current list and make it easier for users to find archived and historical tickets.

## Creation of user groups
User groups provide access control and allow certain users permission and restrictions for others. Users can be assigned groups and groups can be assigned permissions this can simplify administration when the portal grows in popularity and provides enhanced security. This way, unauthenticated user could be able to see tickets, but still be restricted on user details on tickets and comments for security purposes. As the portal develops, user groups can expand to more than Requestors and Fixers and the groups could evolve and be split up, for example, cleaning jobs are only shown to users in the cleaning user group. This idea has big potential and can offer huge flexibility to the site.

# Testing
## Manual Testing
I have conducted an extensive list of manual testing, It includes all buttons and pages to ensure the function as desired and without errors.

### All pages views - no user logged in
| Action taken                     | Expected result                             | Actual result                              | Outcome |
|---------------------------------|---------------------------------------------|--------------------------------------------|---------|
| Get started here! button clicked| User is directed to login page              | Action matched expected result            | Pass    |
| Ticket option selected in nav bar | User is directed to login page             | Action matched expected result            | Pass    |
| Profile selected in navbar       | Shows, register and login options           | Action matched expected result            | Pass    |
| Register selected                | Directs user to register for a new account | Action matched expected result            | Pass    |
| Login Selected                   | Directs user to sign in to their account   | Action matched expected result            | Pass    |
| New user account created         | Account created with success notification | Action matched expected result            | Pass    |
| Existing user logged in         | Log on successful, success message shown   | Action matched expected result            | Pass    |

### Home and About Views - user logged in

| Action taken                              | Expected result                           | Actual result                            | Outcome |
|-------------------------------------------|-------------------------------------------|------------------------------------------|---------|
| 'Create or Amend tickets here' button selected | Directed to List of tickets page      | Action matched expected result          | Pass    |
| Tickets selected in navbar                | Directed to List of tickets page         | Action matched expected result          | Pass    |
| Profile selected in navbar                | Shows About and Logout options           | Action matched expected result          | Pass    |
| About option selected                     | User directed to About View page         | Action matched expected result          | Pass    |
| About Edit button selected                | About Edit view shown                     | Action matched expected result          | Pass    |
| About Edit save changes incomplete form   | 'Fill in empty box' alert shows, no save | Action matched expected result          | Pass    |
| About Edit save changes complete form     | Save completed with success alert        | Action matched expected result          | Pass    |

### Ticket list Views - user logged in

| Action taken                              | Expected result                           | Actual result                            | Outcome |
|-------------------------------------------|-------------------------------------------|------------------------------------------|---------|
| Sort by High priority selected            | Tickets shown from high to low priority, with secondary filter of oldest ticket created first | Action matched expected result | Pass |
| Sort by Low priority selected             | Tickets shown from low to high priority, with secondary filter of oldest ticket created first | Action matched expected result | Pass |
| Sort by newest created                    | Tickets shown with newest tickets first in any priority | Action matched expected result       | Pass |
| Sort by oldest created                    | Tickets shown with oldest tickets first in any priority | Action matched expected result       | Pass |
| Sort by completed tickets                 | Only tickets completed are shown         | Action matched expected result          | Pass |
| Show only my tickets toggle is selected   | Only tickets raised by user logged in are shown | Action matched expected result     | Pass |

### Create/Update/Delete Ticket View - user logged in

| Action taken                              | Expected result                           | Actual result                            | Outcome |
|-------------------------------------------|-------------------------------------------|------------------------------------------|---------|
| Create new ticket button selected         | Opens a Create new ticket view            | Action matched expected result          | Pass    |
| Create ticket successfully                | Directed to ticket list view after ticket submitted, with success message | Action matched expected result | Pass |
| Create duplicate ticket                   | Ticket not submitted and error message shown | Action matched expected result       | Pass |
| Create empty ticket                       | 'Please fill in this field' error message shown for all boxes | Action matched expected result  | Pass |
| Update Ticket Selected                    | Update Ticket view, pre-populated with existing ticket data for editing | Action matched expected result | Pass |
| Update other users tickets                | Update option not visible or available for other user tickets | Action matched expected result  | Pass |
| Update Change details selected           | Ticket detail view, with success message, updated on field updated with time/date | Action matched expected result | Pass |
| Delete ticket selected                    | Directs to Delete Ticket View, with confirmation page | Action matched expected result         | Pass |
| Confirm ticket delete                     | Redirected to Ticket List View, success message shown. Ticket not found in ticket list. | Action matched expected result | Pass |

### Comments - user logged in

| Action taken                              | Expected result                           | Actual result                            | Outcome |
|-------------------------------------------|-------------------------------------------|------------------------------------------|---------|
| Comment added to ticket                   | Comment added and success message shown, user and time/date of post shown | Action matched expected result | Pass |
| Delete comment selected                   | Alert to confirm comment delete is shown  | Action matched expected result          | Pass    |
| Delete comment confirmation               | Ticket detail view is shown and success message. Deleted comment not shown on ticket | Action matched expected result | Pass |

### Ticket Completion - User logged in

| Action taken                              | Expected result                           | Actual result                            | Outcome |
|-------------------------------------------|-------------------------------------------|------------------------------------------|---------|
| Ticket complete checkbox selected          | Checkbox changes state                    | Action matched expected result          | Pass    |
| Ticket Complete Apply button              | Ticket completed, success message shown. Completed by field populated. Complete time and date populated. | Action matched expected result | Pass |

## Validator testing
##### HTML & CSS
HTML and CSS files successfully run through [Offical W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fproject-4-savvy-cfe8d435fa81.herokuapp.com%2F) with no errors found.

##### Python Linter
No errors found, [CI Python linter](https://pep8ci.herokuapp.com/#) used.

## Bugs
### Non functional 2-step process
Situation - Using a 2 step process with a checkbox and an Apply button to complete a ticket when in Ticket Detail View. Currently, Check box is ticked, apply button is pressed. Ticket marked as complete
Issue - When the checkbox isn't touched, the apply button is pressed and the ticket unchecks and marked as incomplete successfully. This negates the need for dual confirmation is the apply button can perform both tasks.
Resolved? - No, Incomplete and unknown fix at this time.

### Update ticket no pre-populated content
Situation - On pressing the Update ticket button, the view doesn't show the current data in the ticket, making it difficult to edit and causing the user to rewrite the whole ticket.
Issue - The form is generated from the same form used for Create Ticket, the pre-populated data is never pulled through because it isn’t present to being with. 
Resolved? - Yes, Create and Update ticket separated, and update ticket pre-populated content is now showing and is editable.

## Deployment
My project is deployed through Heroku can be found [here](https://project-4-savvy-cfe8d435fa81.herokuapp.com/)
1. To set up the code to deploy, I used my existing account with Heroku and created a new Heroku App
2. Set deployment method of GitHub and connected my new App to my GitHub profile.
3. Within my project code, I created a Procfile in the root directory which specifies the commands executed when the app starts up.
4. Added Heroku to my list of 'Allowed Hosts' in settings.py
5. In Heroku, I configured the secret key and database URL to match my project.
6. Manually deployed my main branch and opened the app through Heroku successfully.  

## Credits
- Bootstrap for the CSS framework
- Django for the web framework
- ElephantSQL for the database management
- Homepage image is from [Pexels](https://www.pexels.com/)
- Wireframes are from [Draw.io](https://app.diagrams.net/)
- fontAwesome for icons
- 

