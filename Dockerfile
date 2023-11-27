FROM python:3.11
COPY requirements.txt .
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt