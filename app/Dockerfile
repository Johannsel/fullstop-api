# pull official base image
FROM ubuntu:latest

# create directory for the app user
RUN mkdir -p /home/app

# create the app user ALPINE
#RUN addgroup -S app && adduser -S app -G app

# create the app user UBUNTU
RUN adduser app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Set DEPS for Huggingfaces
ENV TRANSFORMERS_CACHE=$APP_HOME/cache/
ENV HF_DATASETS_CACHE=$APP_HOME/cache/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# install dependencies ALPINE
#RUN apk update && apk add build-base gcc gfortran g++ musl-dev linux-headers rust cargo wget
#RUN apk add     freetype-dev libpng-dev openblas-dev

# install dependencies UBUNTU
RUN apt update && apt install -y libsasl2-dev libldap2-dev libssl-dev libsnmp-dev
#RUN apk add     freetype-dev libpng-dev openblas-dev

# Install python/pip ALPINE
#ENV PYTHONUNBUFFERED=1
#RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
#RUN python3 -m ensurepip
#RUN pip3 install --no-cache --upgrade pip setuptools

# Install python/pip UBUNTU
ENV PYTHONUNBUFFERED=1
RUN apt install -y python3 python3-dev python3-pip && ln -sf python3 /usr/bin/python
#RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# lint
#RUN pip install flake8
#COPY . /usr/src/app/
#RUN flake8 --ignore=E501,F401 .

# Torch
RUN pip3 install torch --extra-index-url https://download.pytorch.org/whl/cpu

# install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# copy project
COPY . $APP_HOME

# fix entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
