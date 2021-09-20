# Base Python Service

## Local Mode

#### Requirements

- Python 3.9
- [Poetry](https://python-poetry.org/docs/#installation)

#### Setup
1. run ```poetry install``` 
2. run ```poetry shell``` (create a venv)

#### Running locally
- ```uvicorn covid_service.main:app```

## Using Docker

#### Requirements
- Docker

#### Running locally

1. ```make build``` 
2. ```make start```


## Documentation
You can see the automatic interactive API documentation using the endpoint: ```/docs```





