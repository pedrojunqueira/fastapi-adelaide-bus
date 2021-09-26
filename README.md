[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# fastapi-adelaide-bus

This repository is a side project to get me into a full stack up using a python FastAPI back end and a little bit of
JavaScrip in the back end.

What the app does is it mimics the Adelaide Metro bus tracker.

The features include

    - Search Bus Stop by name or address in a autocomplete search bar
    - Check the scheduled next incoming bus routes for the stop
    - Show Live data from Adelaide Metro if exist
    - Plot incoming bus in a map relative to the bus you selected

I have not deployed in a server yet.

Data is stored in a MongoDB

The application is packed in Docker and deployed with docker-compose

To launch the app without data here is the instruction

## Usage

### Download the repository

```bash
git clone https://github.com/pedrojunqueira/fastapi-adelaide-bus.git
cd fastapi-adelaide-bus
```

### Create an .env file

```bash
touch .env
echo MONGODB_URL=mongodb://db:27017/demo_bus >> .env
```

You would need docker installed to run the app in containers

### Start network of containers

```bash
docker-compose up --build
```

app will run on port `80` got to [http://0.0.0.0/](http://0.0.0.0/)

## How to add data to mongo

TODO
