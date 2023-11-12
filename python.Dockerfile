FROM python:3.10-alpine AS base 

RUN apk update && apk add bash curl wget

# actualizar pip e instalar poetry
RUN python -m pip install -U pip 
RUN python -m pip install poetry==1.7.0

WORKDIR /project 

COPY . .

# no hace falta usar venv en docker 
RUN poetry config virtualenvs.create false && \
  poetry install --no-interaction --no-ansi


