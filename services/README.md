# Installation

1. Install django `python -m pip install Django`
2. Show the django version `python -m django --version`
3. Run `django-admin startproject main`
4. Rename `main` root folder to `src` with the command `mv ./main ./src`
5. Run `cd src`
6. Run `python manage.py migrate`
7. Run `python manage.py startapp base`
8. `python manage.py makemigrations base`
9. `python manage.py createsuperuser`
10. Run `python manage.py runserver`
