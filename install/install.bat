cd /d "%~dp0"

cd..

cls

pip install -r requirements.txt

Python

from rtbb import app, db

Command: app.app_context.push()

Command: db.create_all()