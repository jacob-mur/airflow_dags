from airflow.sdk import Asset, dag, task
from pendulum import datetime, duration

@dag(
    start_date=datetime(2025, 4, 22),
    schedule="@daily",
    doc_md=__doc__,
    default_args={"owner": "Jacob", "retries": 3},
    tags=["example"],
)

def podman_runner():

    # pull image
    @task.bash
    def pull_image(image_name: str = 'alpine:3.22.4') -> None:
        #return "echo pulling image"
        return f'podman pull "{image_name}"'    
    
    # run image
    @task.bash
    def run_image(image_name: str = 'alpine:3.22.4') -> None:
        #return "echo running image"
        return f'podman run --rm --privileged alpine:3.22.4 echo "hello world"'

    # calling task
    pull_image()
    run_image()