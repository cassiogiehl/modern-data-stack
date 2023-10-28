from airflow.decorators import dag
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from datetime import datetime

from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig


ID_CONN_AIRBYTE = "ddaa62f3-213f-437f-abeb-861a8b4e9828"
ID_CONN_POSTGRES = "dw_connection"

DB_NAME = "data_warehouse"
DW_SCHEMA = "public"

ROOT_PATH_DbT_PROJECT = "/opt/airflow/dags/dbt/"
DBT_LAUNCHES_COST_PATH = ROOT_PATH_DbT_PROJECT + "spacex_transform/"


profile_config = ProfileConfig(
    profile_name="data_warehouse",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id=ID_CONN_POSTGRES,
        profile_args={
            "schema": DW_SCHEMA,
            "dbname": DB_NAME
        },
    ),
)

@dag(
    'spacex-pipeline', 
    description='SpaceX pipeline ingestion',
    schedule_interval='1 * * * *',
    start_date=datetime(2023, 10, 17), 
    catchup=False
)
def dag_spacex_lauches_cost():
    api_to_dw = AirbyteTriggerSyncOperator(
        task_id="api_to_dw",
        airbyte_conn_id="airbyte_connection",
        connection_id=ID_CONN_AIRBYTE,
        asynchronous=False,
        timeout=3600,
        wait_seconds=10
    )

    dbt_launches_cost = DbtTaskGroup(
        group_id="launches_cost",
        project_config=ProjectConfig(DBT_LAUNCHES_COST_PATH),
        profile_config=profile_config,
        default_args={"retries": 2},
    )

    api_to_dw >> dbt_launches_cost

dag_spacex_lauches_cost()