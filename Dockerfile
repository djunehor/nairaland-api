FROM python:3.5
LABEL maintainer djunehor

COPY requirements.txt /app
ADD app /

WORKDIR /app

EXPOSE 5000

CMD python app.py