#!/usr/bin/bash

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
