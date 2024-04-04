FROM python:3.9

RUN apt-get update && apt-get install -y wget

WORKDIR /app

COPY ingest_data.py .
COPY taxi_zone_lookup.csv .
COPY ingest_zone.py .

RUN pip install pandas sqlalchemy psycopg2

CMD ["python", "ingest_data.py"]