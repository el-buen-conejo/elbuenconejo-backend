#!/usr/bin/bash 
source /home/ubuntu/env/bin/activate
cd /home/ubuntu/elbuenconejo-backend
python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
