from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

with DAG(
    dag_id="pure_kubernetes_pod_operator_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["k8s", "operator"],
) as dag:

    run_docker_image = KubernetesPodOperator(
        task_id="run_native_container",
        # The Docker image you want to execute (no Python required)
        image="barbasol/hello_world:1.0.0",
        namespace="bsc",
        in_cluster=True,
        
        # safety configuration
        do_xcom_push=False,             # Prevents Airflow from looking for an XCom output file
        get_logs=True,                  # Streams the container's stdout/stderr to Airflow logs
        is_delete_operator_pod=True,    # Automatically cleans up the pod after it finishes
    )