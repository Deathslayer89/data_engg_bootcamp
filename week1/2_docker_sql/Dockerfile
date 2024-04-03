FROM python:3.9

RUN apt-get update && apt-get install -y wget

WORKDIR /app

COPY ingest_data.py .


RUN pip install pandas sqlalchemy psycopg2

CMD ["python", "ingest_data.py"]