#!/usr/bin/bash
export DJANGO_SETTINGS_MODULE=rabbits_farm.prod_settings
sudo cp /home/ubuntu/elbuenconejo-backend/gunicorn/gunicorn.socket  /etc/systemd/system/gunicorn.socket
sudo cp /home/ubuntu/elbuenconejo-backend/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
