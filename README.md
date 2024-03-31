# Service Savvy

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

## Wireframes

![homepage drawio](https://github.com/meganw22/service-savvy/assets/141934888/5b25dc16-9bb7-410c-80c1-6f46753929e7)

![ticket list drawio](https://github.com/meganw22/service-savvy/assets/141934888/44da37d1-e83b-4fc6-928c-2b2b322a6f90)

![ticket detail drawio](https://github.com/meganw22/service-savvy/assets/141934888/10db718f-4a60-4153-aa27-d45db74cc61d)

![create ticket drawio](https://github.com/meganw22/service-savvy/assets/141934888/547e8c76-3d35-48e9-907c-aaeda5a86756)

![update ticket drawio](https://github.com/meganw22/service-savvy/assets/141934888/c71b40ff-9ce0-4e60-8e32-9a46bb2857ce)

## Features
Service savvy is fully responsive and easy for new users to navigate. It required users to be authenticated when viewing and amending details but the homepage is avaliable for all users to view.

### Nav Bar
The nav bar includes the logo, and nav links for Home, Tickets and User Profile page.
Unathenticaed view of nav bar:
![image](https://github.com/meganw22/service-savvy/assets/141934888/fd551651-c953-41d1-88df-97f0dc9a43f2)

Authenticated view of nav bar:
![image](https://github.com/meganw22/service-savvy/assets/141934888/90b1d7e2-dd6a-4edc-bbb0-4c4c75250eef)

### Footer
the footer is consistent throughout the webpages and is responsive:
![image](https://github.com/meganw22/service-savvy/assets/141934888/4a5a2a15-7855-4a56-afef-ac911d30ee42)

### Colour scheme
![image](https://github.com/meganw22/service-savvy/assets/141934888/49b55da4-0a82-4fa2-9490-45f420ab4f86)

## Homepage
The homepage displays a simple structure, welcoming users to the portal. It contains hyperlinks to prompt the user into creating or loggin in to an account before they are able to view the rest of the website content. 
Further down the homepage, there is a section containing emergency information for a user to contact. It is displayed in obvious and large formatting.

Unauthenticated display

![image](https://github.com/meganw22/service-savvy/assets/141934888/6182be73-72ab-47dc-90c0-10ad92c03de2)

Authenticated display

![image](https://github.com/meganw22/service-savvy/assets/141934888/ab97e897-4e22-4780-9455-0a22a54bb5fc)

### Register
The user is directed to registion form which is provided by Django. It allows a user to create an account with prompts and suggestion for a secure password. 

![image](https://github.com/meganw22/service-savvy/assets/141934888/4a21c23d-0bf5-4ba1-b283-3aaafe78df4a)

### Login
The Login view is provided by Django and allows the user to log into their account. With this, the user will now have authentication and will be able to see more aspects of the website that were limited to them before. The user is shown a successful log in alert at the top of the page.

![image](https://github.com/meganw22/service-savvy/assets/141934888/af6956d1-e5fe-492d-8005-aaddcb3a6b32)

### Sign out
The sign out view is a 2 step process to confirm the user wants to log out. The user is redirected to the homepage and is shown a successful 'log out' alert at the top of the screen.

![image](https://github.com/meganw22/service-savvy/assets/141934888/bde942f0-d615-476c-9091-2e08b55cad55)

## Tickets 
Within the maintenance portal, a ticket raised means a problem has occured. The user creating the ticket will fill in the details and submit it, wsending it to the ticket list view. All authenticated user can see all tickets. 

### List
The ticket list, shows all created tickets raised by users. The tickets are sorted, by default, in order of highest priority first with a secondary filter, oldest created. This is useful for maintenance members who want a quick view of which tickets are the higher priority tickets and what needs addressing first.

![image](https://github.com/meganw22/service-savvy/assets/141934888/8660f842-22b0-4301-8972-b39f99984925)

The sort filter dropdown has multiple options allowing flexible view of tickets. The tickets listed are all incompleted tickets and are awaiting fixing. All completed tickets are seperated through another filter called 'Completed'
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
the Ticket detail view is displayed when a user opens a created ticket. It provides the details of the ticket and has some targeted authentication rules that only the user raising the ticket can see.

![image](https://github.com/meganw22/service-savvy/assets/141934888/2ce2c561-9503-41d7-b80b-346718ae1251)

If a user is not the creator of a ticket they cannot edit, delete or complete the ticket.

![image](https://github.com/meganw22/service-savvy/assets/141934888/fc063f2f-0a07-4ec1-b138-6673a1cf8836)

### Update Tickets
Only the authenticated user who created the ticket, can update the ticket. For all other users, the update button not displayed or avaliable.
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
Only the authenticated user who created the ticket, can delete the ticket. For all other users, the delete button is not displayed or avaliable.
the delete ticket process is a 2-step verification where the user is directed to a new page to confirm ticket requires deleting before they are re-directed back to the tickets list page.
![image](https://github.com/meganw22/service-savvy/assets/141934888/bb836727-84d9-4f16-843d-ee8d0ad8a69a)

### Profile details 
When a user is authenticated they can navigate to their about page to populate and manage their own details.
![image](https://github.com/meganw22/service-savvy/assets/141934888/57412db8-effc-4cba-bc64-ee0c1d322b53)


## Future Implementation
### Utilise the Archive model
Creating an Archive model can be benefical for data organisation, performance and user experience. I have implemented a form of separation of completed tickets from incomplete tickets but and archive feature can keep the database more organised and easier to manage. For performance purposes, a separate database to hold the completed data would benefit the performance greatly by reducing the size of the active ticket database. Finally, user experience will improve as the new model will de-clutter the current list and make it easier for users to find archived and historical tickets.

### Creation of user groups
User groups provide access control and allow certain users permission and restrictions for others. Users can be assigned groups and groups can be assigned permissions this can simplify administration when the portal grows in popularity and provides enhanced security. This way, unauthenticated user could be able to see tickets, but still be restricted on user details on tickets and comments for security purposes. As the portal develops, user groups can expand to more than Requestors and Fixers and the groups could evolve and be split up, for example, cleaning jobs are only shown to users in the cleaning user group. This idea has big potential and can offer huge flexibilty to the site.

## Testing
### new page

## deployment

## Credits
### Content
### Media

