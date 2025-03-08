from airflow.decorators import dag
from airflow.operators.smooth import SmoothOperator
from datetime import datetime


@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["smooth"],
)
def smooth():
    video = SmoothOperator(
        task_id="youtube_video"
    )


smooth()
