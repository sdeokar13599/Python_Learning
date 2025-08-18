from diagrams import Diagram
from diagrams.gcp.storage import Storage
from diagrams.gcp.analytics import Bigquery, Composer

with Diagram("GCP Data Pipeline", show=True):
    gcs = Storage("GCS")
    bq = Bigquery("BigQuery")
    airflow = Composer("Airflow")
    gcs >> bq
    airflow >> bq