cd /d "%~dp0"

cd..

cd rtbb

cls

pybabel extract -F babel.cfg -o messages.pot .
pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .

pybabel update -i messages.pot -d translations -l en
pybabel update -i messages.pot -d translations -l pt
pybabel update -i messages.pot -d translations -l de

pybabel compile -f -d translations

pause