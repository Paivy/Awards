## AWARDS

### Author

[Paivy Eshirera](https://github.com/Paivy/Awards.git.)

### Description

This application that allows a user to post their projects they have created and get them reviewed by fellow peers and vote according to how they feel towards a particular project.

## BDD
| Behaviour                                                                   | Input                                        | Output                                                              |
|-----------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------|
|  The Page loads the homepage                                                |  On application load                         |  Navigate to the home/index page displaying all the projects        |
|  Navigate to signup page when SignUp is clicked on the navigation bar:      |  User successfully registers                 |  User redirected to the login page                                  |
|  Navigate to the login page when Login is clicked on the navigation bar:    |  Click on Login on the Navbar dropdown menu  |  User can view a specific image with all its details                |
|  User is redirected to the specific profile page                            |  User clicks on profile icon                 |  User Redirected to the index page which displays all projects      |
|  The program directs the user to a review page with a single project details and vote button:     |  Click on Review Project  |  User redirected to the single project review page with the project's description and a vote button|
|  Program navigates to the vote modal form                                   |  Click on Vote button                        |  A vote modal form pops up                                          |
|  Program should load the live site on a new tab                             |  Click on View Site/Live Project Link           |  Live site of a specific project loads                           |
|  User is redirected to the Profile Page                                   |  User clicks Profile on the Navbar dropdown       |  Program opens Profile page with all users information including their projects   |


## Setup Instructions

Use the folllowing commands for the project to be in use.
* git clone https://github.com/Paivy/Awards.git.
* install `python 3.8`
* Install [Postgresql](https://www.postgresql.org/download/)
* cd AWARDS
* Navigate to the virtual environment using `source virtual/bin/activate`
* `atom .`  //For those using atom text editor.
* `code .`  //For those using Visual Studio editor.


## Install dependancies

Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`

### Create the Database
```
psql
CREATE DATABASE <name that you want your database to be named>;
```
- Run `python3.8 manage.py runserver`
- Access the application on this localhost address `http://127.0.0.1:8000`

## Link to live site



## Technologies used

1. Python 3.8 
2. Bootstrap
3. HTML
4. CSS
5. Postgresql
6. Bootstrap
7. Django Framework

## Contact
- mobile :
- email : 
- slack : 

### License  & Copyright information
Copyright (c) 2022 Paivy Eshirera

### API ENDPOINTS
### Profile endpoint
http://127.0.0.1:8040/api/profile/

### Project endpoint
http://127.0.0.1:8040/api/projects/
