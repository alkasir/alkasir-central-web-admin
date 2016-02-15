FROM python:3.5.0
ENV PYTHONUNBUFFERED 1

workdir /centraladmin/

add requirements*.txt /centraladmin/
run pip install --no-cache-dir -r requirements-dev.txt
run pip install --no-cache-dir -r requirements-dev-extra.txt

add ./ /centraladmin/

expose 8000
cmd ./manage.py runserver 0.0.0.0:8000
