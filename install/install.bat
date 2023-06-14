cd /d "%~dp0"

cd..

cls

pip install -r requirements.txt

Python

from rtbb import app, db

app.app_context.push()

db.create_all()

exit()