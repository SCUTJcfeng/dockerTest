FROM python:3.6.4-alpine

WORKDIR /app/app

RUN python3 -m pip install pipenv
RUN pipenv install --ignore-pipfile
CMD ["pipenv", "run", "python3", "main.py"]
