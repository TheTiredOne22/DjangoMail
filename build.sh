pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigration
python manage.py migrate