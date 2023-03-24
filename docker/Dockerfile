FROM python:3.11-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system app && adduser --system --group app

ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

COPY ../requirements.txt .
RUN pip install -r requirements.txt

COPY .. $APP_HOME

RUN chown -R app:app $APP_HOME

USER app
