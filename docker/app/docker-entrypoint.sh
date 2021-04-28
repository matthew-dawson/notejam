#! /bin/bash

set -ex

# Create the database schema
python3 db.py

# TODO: Utilize a WSGI server to host the app
python3 runserver.py
