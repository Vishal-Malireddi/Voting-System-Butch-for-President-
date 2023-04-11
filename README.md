# Voting-System-Butch-for-President-
This is a repository for the project for CPTS 322

## Project Structure
virtual_env: the python virtual environment (stores all the packages needed in the directory, this helps to avoid package conficts)

- project/    &emsp;&emsp;&emsp;&emsp;    (the root directory for our project)
    - manage.py    &emsp;&emsp;&emsp;    (commandline utility for django)
    - project/    &emsp;&emsp;    (the actual python package for our project)
        - \_\_init\_\_.py    &emsp;&emsp;&emsp;&emsp;    (tells the python directory that it is a python package)
        - settings.py    &emsp;&emsp;    (config for django project)
        - urls.py    &emsp;&emsp;&emsp;&emsp;    (url declarations, the "table of contents")
        - asgi.py    &emsp;&emsp;&emsp;&emsp;    (entry point for ASGI-compatible web servers)
        - wsgi.py    &emsp;&emsp;&emsp;&emsp;    (entry point for WSGI-compatible web servers
   - voting_system/    &emsp;&emsp;&emsp;&emsp;    (this is where our application is aka "our stuff")
		- \_\_init\_\_.py
	    - admin.py    &emsp;&emsp;&emsp;&emsp;     (register models with django admin here, admin is pre-built)
	    - apps.py    &emsp;&emsp;&emsp;&emsp;     (deals with the configuration of the apps)
	    - migrations/    
	        - \_\_init\_\_.py
	    - models.py    &emsp;&emsp;&emsp;&emsp;     ("Models are basically the blueprints of the database we are using and hence contain the information regarding attributes and the fields etc of the database." (Nishant, 2020))
	   - tests.py    &emsp;&emsp;&emsp;&emsp;     (Where we test our code)
	   - urls.py    &emsp;&emsp;&emsp;&emsp;     (Links the views to the host web URL)
	    -	views.py&emsp;&emsp;&emsp;&emsp;     ("Views are a user interface for what we see when we render a Django Web application." (Nishant, 2020)

## Launching the Application
1. Make sure you have installed Django
2. Make sure you are in the directory with the manage.py file
3. run `python manage.py runserver`
4. Make sure the url ends with a valid url pattern


## Sources
### used for explaining file herarchy and helping us understand django
https://www.askpython.com/django/django-app-structure-project-structure
https://docs.djangoproject.com/en/4.2/intro/tutorial01/
