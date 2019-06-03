FROM python:3.6.4-alpine

WORKDIR /

RUN pip install pipenv
RUN pipenv install
CMD ["pipenv", "run", "python3", "main.py"]
