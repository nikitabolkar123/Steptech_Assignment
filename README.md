# Steptech_Assignment
#The brief README file that includes instructions on how to set up and run your django applications And git workflow
git clone https://github.com/nikitabolkar123/Steptech_Assignment.git
python -m venv venv
source venv/bin/activate  
pip freeze > requirement.txt
pip install django psycopg2
django-admin startproject steptech_app .
python manage.py startapp user
python manage.py makemigrations
python manage.py migrate
git checkout -b stoptech_assignment
git add .
git commit -m "[Nikita] Added. users data"
git push origin steptech_assignment
python manage.py runserver


#database 
The database schema for the "users" table is as follows:
Table Name: users

Columns:
- id (int, primary key)
- name (varchar)
- email (varchar)
- role (varchar)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'steptech_db',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#Document any additional dependencies or setup requirements.
asgiref==3.7.2
Django==4.2.3
psycopg2==2.9.6
sqlparse==0.4.4
typing_extensions==4.7.1
tzdata==2023.3

#Create a MySQL database named "users" with the following schema:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50)
);
#You can  use Django's migration to create the database:
python manage.py makemigrations
python manage.py migrate

#INSERT INTO users (name, email, role) VALUES
    ('nikita'', 'nikita@gmail.com', 'python developer'),
    ('priya', 'priya@gmail.com', 'java developer'),
    ('ram', 'ram@gamil.com', 'hr');

 # Retrieve All Users from "users" table:
SELECT * FROM users;
#Retrieve a Specific User by ID
SELECT * FROM users WHERE id = <user_id>;

