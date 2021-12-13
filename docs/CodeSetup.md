# Code Setup

## Intial Setup

- Create a virtual environment for python: `virtualenv venv`
- Add python gitignore file using python: `npx gitignore python`
- Initialize git repository - `git init`
- Configure remote repository: `git remote add origin https://github.com/id-shiv/orion.git`
- Confirm the remote repository settings: `git remote -v`
- Install required packages: `pip install django djangorestframework django-environ psycopg2-binary django-autoslug flake8 black`
- Save the required packages: `pip freeze > requirements.txt`
- Verify the installed packages version: `pip list`
- Add `.vscode` to `.gitignore`
- Setup Django Project: `django-admin startproject config .`
- Setup `.env` file
