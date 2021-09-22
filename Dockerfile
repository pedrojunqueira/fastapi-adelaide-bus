FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# set timezone to adelaide
RUN unlink /etc/localtime \
    && ln -s /usr/share/zoneinfo/Australia/Adelaide /etc/localtime

# copy project

COPY ./app /app