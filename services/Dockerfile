FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /usr/src/app/src/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh","-c","python manage.py migrate && gunicorn -b 0.0.0.0:8000 main.wsgi --workers=4"]
