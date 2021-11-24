FROM python:3.10.0b2
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
RUN pipenv install --deploy --system --skip-lock --dev
COPY . /code/