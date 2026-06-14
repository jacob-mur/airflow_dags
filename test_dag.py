from airflow.sdk import Asset, dag, task
from pendulum import datetime, duration

@dag(
    start_date=datetime(2025, 4, 22),
    schedule="@daily",
    doc_md=__doc__,
    default_args={"owner": "Jacob", "retries": 3},
    tags=["example"],
)
def test_dag():
    @task.kubernetes(image="ubuntu:24.04",
                     name="k8s-task-worker",
                     namespace="bsc",
                     in_cluster=True,
                     get_logs=True,)
    
    def echo_hello_world():
        """
        This function body executes inside the Kubernetes pod.
        Standard output is captured and forwarded to the Airflow task log.
        """
        print("hello world")
 
    # Invoke the task (creates the pod when the DAG runs)
    echo_hello_world()
    
test_dag()