from datetime import datetime
from airflow import DAG
# from cosmos import DbtTaskGroup, ProjectConfig #, ExecutionConfig
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

# ID_CONN_AIRBYTE = "d0ecad32-7bb3-403b-9f28-a2fad0868835" # minio
ID_CONN_AIRBYTE = "ddaa62f3-213f-437f-abeb-861a8b4e9828"


with DAG(
    'spacex-pipeline', 
    description='SpaceX pipeline ingestion',
    schedule_interval='1 * * * *',
    start_date=datetime(2023, 10, 17), 
    catchup=False):

    api_to_dw = AirbyteTriggerSyncOperator(
        task_id="api_to_dw",
        airbyte_conn_id="airbyte_connection",
        connection_id=ID_CONN_AIRBYTE,
        asynchronous=False,
        timeout=3600,
        wait_seconds=10
    )

    # dbt_launches_cost = DbtTaskGroup(
    #     project_config=ProjectConfig("dbt/spacex_transform/"),
    #     default_args={"retries": 2},
    # )

    api_to_dw #>> dbt_launches_cost
