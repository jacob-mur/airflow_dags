from airflow.sdk import Asset, dag, task
from pendulum import datetime, duration

@dag(
    start_date=datetime(2025, 4, 1),  # date after which the DAG can be scheduled
    schedule="@daily",
    max_consecutive_failed_dag_runs=5,  # auto-pauses the DAG after 5 consecutive failed runs, experimental
    doc_md=__doc__, 
    default_args={
        "owner": "jmurray",  # owner of this DAG in the Airflow UI
        "retries": 3,  # tasks retry 3 times before they fail
        "retry_delay": duration(seconds=5),  # tasks wait 30s in between retries
    },  # default_args are applied to all tasks in a DAG
    tags=["testing", "podman"],  # add tags in the UI
    is_paused_upon_creation=True, # start running the DAG as soon as its created
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