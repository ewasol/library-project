FROM python:3.11-alpine
ENV FLASK_APP=src.run
WORKDIR /src
ENV PYTHONPATH=../
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY src/ src/
