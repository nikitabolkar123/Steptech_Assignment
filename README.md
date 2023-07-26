# Steptech_Assignment
git clone https://github.com/nikitabolkar123/Steptech_Assignment.git
cd your-django-app

python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
pip install django psycopg2
django-admin startproject steptech_app .
python manage.py makemigrations
python manage.py migrate
git checkout -b stoptech_assignment
git commit -m "users data"
git push origin steptech_assignment


