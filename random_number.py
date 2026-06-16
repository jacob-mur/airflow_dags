from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

with DAG(
    dag_id="random_number_runner",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["k8s", "random_number"],
) as dag:

    run_docker_image = KubernetesPodOperator(
        task_id="random_number_run",
        # The Docker image you want to execute (no Python required)
        image="barbasol/random_number:1.0.0",
        namespace="bsc",
        in_cluster=True,
        # safety configuration
        do_xcom_push=False,             # Prevents Airflow from looking for an XCom output file
        get_logs=True,                  # Streams the container's stdout/stderr to Airflow logs
        is_delete_operator_pod=True,    # Automatically cleans up the pod after it finishes
    )