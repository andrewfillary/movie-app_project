# Movie app project (They're here!)

## Overview

### What does it do?
"They're here!" is a movie database app. Users can browse movie reviews, statistics
and subscribe to the magazine that is available to download in PDF format when
succesfully logged in.

### How it works...
Created using Python's Django framework, the MVC structure seperates logic and design, and provides url routing, 
making code easily accessible and tidy. The source code and SQL database are deployed to Heroku, users with adminstrative 
privelages may add/edit objects (i.e. magazines, movies) from django's built in admin panel. 

## Technologies
- **Django** - Python based MVC framework. 
- **Heroku** - Code and database deployment solution.

### Heroku (third party packages)
- **DJ Database URL** - Database URL configuration.
- **Whitenoise** - Static file routing.

## Requirements
If you would like to run this app on your own server, first fork the repo into a local directory, then install the **requirements.txt** file.

**Important!** This app is a course assignment, therefore the subscription is for demonstration only.
To register you must fill out the subscripition form in full and use the 16 digit card number
reserved for the stripe sandbox payment process.

**Stripe 16 Digit Card No.** (for registration) <br />
4242 4242 4242 4242

## Live Site
http://movie-app-project.herokuapp.com

