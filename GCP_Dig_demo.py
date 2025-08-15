from diagrams import Diagram
from diagrams.gcp.storage import Storage
from diagrams.gcp.analytics import Bigquery

with Diagram("GCP Architecture", show=True):
    gcs = Storage("GCS",fontsize="16")
    bq = Bigquery("BigQuery",fontsize="16")
    gcs >> bq       # This should always draw a line!
