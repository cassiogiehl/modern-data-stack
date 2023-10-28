# Modern Data Stack

## Análise de custo de lançamento de foguetes Space X
* Airbyte
* Airflow
* DBT (Data Build Tool)

# Configuração e execução

## Dependências
* Docker
* Docker Compose

## Instale e execute o Airbyte
* [Tutorial de instalação Airbyte](https://docs.airbyte.com/deploying-airbyte/local-deployment)

## Execute o container com os componentes da aplicação
```
docker compose up -d
```

## Configure a connection do airflow com aibyte
* [Airflow and Airbyte OSS - Better Together](https://airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together)
* [Using the Airbyte Operator to orchestrate Airbyte OSS](https://docs.airbyte.com/operator-guides/using-the-airflow-airbyte-operator)

## Configure a connection do airflow com o dw (Postgres)
* [Orchestrate DBT Core jobs with Airflow and Cosmos](https://docs.astronomer.io/learn/airflow-dbt)

## Configure os sources/sinks do airbyte
* [Create source conncetion SpaceX-API](https://docs.airbyte.com/integrations/sources/spacex-api)
* [Create sink conncetion Postgres](https://docs.airbyte.com/integrations/destinations/postgres)

