SHELL := /bin/bash

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'


init: install migrate

install:
	pip3 install --user -r requirements.txt

run:
	python ./src/manage.py runserver

test:
	python ./src/manage.py test

migrate:
	python ./src/manage.py makemigrations
	python ./src/manage.py migrate

superuser:
	(DJANGO_SUPERUSER_PASSWORD=root python ./src/manage.py createsuperuser --email=root@root.com --username=root --noinput)