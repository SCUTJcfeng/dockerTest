FROM python:3.6.4-alpine

WORKDIR /app
COPY ./app/ /app
COPY ./Pipfile.lock /app

RUN pip install pipenv
RUN pipenv install --ignore-pipfile
CMD ["pipenv", "run", "python3", "main.py"]
