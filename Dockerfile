FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    make \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir wheel \
    && pip install --no-cache-dir cmake \
    && pip install --no-cache-dir pandas \
    && pip install --no-cache-dir boto3 \
    && pip install --no-cache-dir minio \
    && pip install --no-cache-dir dbt-core \
    && pip install --no-cache-dir dbt-trino \
    && pip install --no-cache-dir dbt-postgres \
    && pip install --no-cache-dir astronomer-cosmos \
    && pip install --no-cache-dir astronomer-cosmos[dbt.postgres] \
    && pip install --no-cache-dir nes-py