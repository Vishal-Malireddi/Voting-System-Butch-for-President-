# Voting-System-Butch-for-President-
This is a repository for the project for CPTS 322

## Project Structure
virtual_env: the python virtual environment (stores all the packages needed in the directory, this helps to avoid package conficts)

- voting_system/                  (the root directory for our project)
    - manage.py                   (commandline utility for django)
    - voting_system/              (the actual python package for our project)
        - __init__.py             (tells the python directory that it is a python package)
        - settings.py             (config for django project)
        - urls.py                 (url declarations, the "table of contents")
        - asgi.py                 (entry point for ASGI-compatible web servers)
        - wsgi.py                 (entry point for WSGI-compatible web servers)
        
