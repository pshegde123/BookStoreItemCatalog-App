# Item Catalog Web App

This is a project for Udacity's [ Full Stack Web Developer Nanodegree Program ](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Description

Using Python3, [Flask](http://flask.pocoo.org/) , [Bootstrap](http://getbootstrap.com/) ,Python SQL toolkit & ORM mapper **SQLAlchemy**(https://www.sqlalchemy.org/), this application displays catalog of a book store and items in the catalog. 
Users can perform CRUD operations on this catalog by logging in the application using their [Google](www.google.com) , [Facebook](www.facebook.com) account login.

## Getting Started
	*You can clone or download this project via [Github] (www.github.com) on your local machine.
		`<$git clone https://github.com/pshegde123/BookStoreItemCatalog-App.git catalog>`
	*This program need to be run on a virtual machine (VM), to setup the VM please check following steps.

### Prerequisites
	*[Git](https://git-scm.com/downloads) : 
	On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash). 
	You will need Git to install the configuration for the VM. 

	*[VirtualBox](https://www.virtualbox.org/wiki/Downloads):
	VirtualBox is the software that actually runs the VM.

	*[Vagrant](https://www.vagrantup.com/downloads.html):
	Vagrant is the software that configures the VM.

	*Run the virtual machine: Using the terminal, change directory to catalog/vagrant (cd fullstack/vagrant), then type `<$vagrant up>` to launch your virtual machine.Once it is up and running, type `<$vagrant ssh>` to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. Change to the /vagrant directory by typing `<cd /vagrant>`. 

### Usage:
	(1) After completing prerequisites, start the application web server by entering
		`<$python application.py>`
		Server will run on port 8000
	(2) On your web browser enter URL *http://localhost:8000*, home page of application will be displayed
    	(3) URL *http://localhost:8000/catalog* will display the default catalog contents from database *catalog.db*
    	(4) After logging in to the application, user can edit,delete only those items which are created by user.

### JSON endpoints available:
	This app provides two JSON endpoints
	(1)/catalog/<int:catalog_id>/JSON 
	(2)/catalog.json
### Files Included:
	(1) application.py : This file contains code for the web server.
	(2) database_setup.py : This file contains table structure for database named catalog.db
	(3) data.py : This file inserts default data in database.
	(4) catalog/templates : This folder contains all the HTML files required for login & CRUD operations.
	(5) catalog/static: This folder contains images displayed on the web page and CSS file.
	(6) Vagrantfile: vagrant config file 
	(7) client_secrets.json : File required for Google API
	(8) fb_client_secret.json: File required for Facebook API
	(9) README.md : readme document
