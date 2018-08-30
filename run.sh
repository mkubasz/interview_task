#!/bin/bash
python3 -m venv myvenv
source myvenv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r ./InterviewCrawler/requirements.txt
pip3 install -r ./InterviewApi/requirements.txt
python3 ./InterviewApi/manage.py makemigrations
python3 ./InterviewApi/manage.py migrate
cd InterviewApi
gunicorn InterviewApi.wsgi --daemon --bind 0.0.0.0:8000
cd ..
python3 ./InterviewCrawler/App.py
