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
		- __init__.py
	    - admin.py
	    - apps.py
	    - migrations/
	        - \_\_init\_\_.py
	    - models.py
	   - tests.py
	    -	views.py

