# PhD Portal
This is the portal for phd admissios of IIT Ropar.

### Prerequisites
- Virtual Environment
- Mysql
- Python 3.7

### Installation Instructions
- activate any virtual environment

- pip install django

- pip install bcrypt

- pip install django[argon2]

- pip install pillow

- pip install django-bootstrap4

- pip install python-dateutil

- pip install django-braces

#### Connecting database with django application
- Insatlling mysqlclient
  - sudo apt-get install libexpat1=2.2.6-2
  - sudo apt-get install libexpat1-dev
  - sudo apt-get install libpython3.7-dev
  - sudo apt-get install python3.7-dev
  - sudo apt-get install python3-dev
  - sudo apt-get install python3-dev libmysqlclient-dev
  - pip install mysqlclient

- Create a mysql database in Mysql shell

- Edit name(line 94) with your databse name, user(line 95) with your mysql username and  password(line 96) in phdadmission/settings.py

### RUNNING Web Application
#### migrating apps
- python manage.py makemigrations accounts

- python manage.py makemigrations dropdown

- python manage.py makemigrations faculty

- python manage.py makemigrations myfiles

- python manage.py makemigrations phdfellows

- python manage.py migrate

#### serving static files
- python manage.py collectstatic

#### Loading data in dropdown tables
- python manage.py loaddata country.json 

- python manage.py loaddata state.json

- python manage.py loaddata ugdiscipline.json

- python manage.py loaddata pgdiscipline.json

- python manage.py loaddata branchqualifyingexamination.json 

- python manage.py loaddata category.json 

- python manage.py loaddata researcharea.json

- python manage.py loaddata typeofwork.json 

#### Creating superuser(admin)
- python manage.py createsuperuser

#### Running
- python manage.py runserver

## Roles
Users can be of three types- student, faculty(staff) and admin. To give staff status to a user admin has to tick on staff status by opening user's account.Similarly admin account can be made. 

## Dropdown
The HTML dropdowns also gets data from database. To add more data in any dropdown(for ex- category), admin can add them by opening them from admin homepage.

## Uploaded files
Uploaded files are saved in phdadmission/media. Announcements(files that are to be displayed in notice board) are saved in phdadmission/media/announcements. OMR Sheets are saved in phdadmission/omr_sheets/YYYY/MM/DD. YYYY/MM/DD is the date when the file were uploaded.

## Editing emails
- To make changes in account activation email edit line 86 of phdadmission/accounts/views.py
- To change account activation email subject edit line 82 of phdadmission/accounts/views.py
- To make changes in password reset email edit phdadmission/templates/registration/password_reset_email.html
- To change account activation email subject edit phdadmission/templates/registration/password_reset_subject.txt
