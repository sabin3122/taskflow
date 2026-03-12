#!/usr/bin/env bash
pip install -r requirements.txt
cd theme/static_src && npm install && npm run build && cd ../..
python manage.py collectstatic --noinput
python manage.py migrate