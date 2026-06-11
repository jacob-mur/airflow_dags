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
    @task.kubernetes(
        image="alpine:3.22.4'",  # The Docker image to spin up
        name="k8s-task-worker",    # Base name for the generated pod
        namespace="bsc",       # Target K8s namespace
        in_cluster=True,           # True if Airflow is already inside the cluster
        # Optional: define resource constraints
        get_logs=True,             # Streams container stdout straight to Airflow logs
    )

# instantiate the dag
test_dag()