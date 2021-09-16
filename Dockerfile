FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app