#!/bin/bash

source venv/bin/activate && FLASK_APP=app/infrastructure/routes.py flask run
