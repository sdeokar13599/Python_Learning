from diagrams import Diagram
from diagrams.gcp.compute import GKE, ComputeEngine
from diagrams.gcp.storage import Storage
from diagrams.gcp.database import SQL
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.analytics import (
    Bigquery,        # alias: BigQuery
    DataCatalog,
    DataFusion,
    Dataflow,
    Datalab,
    Dataprep,
    Dataproc,
    Genomics,
    Pubsub           # alias: PubSub
)

from diagrams.gcp.database import (
    Bigtable,        # alias: BigTable
    Datastore,
    Firestore,
    Memorystore,
    Spanner,
    SQL
)

from diagrams.gcp.storage import (
    Filestore,
    PersistentDisk,
    Storage           # alias: GCS
)


with Diagram("GCP Architecture Example", show=True):  # show=True opens image after generation
    # gke = GKE("GKE Cluster")
    # compute = ComputeEngine("Compute VM")
    # storage = Storage("Cloud Storage")
    # sql = SQL("Cloud SQL")
    # pubsub = PubSub("Pub/Sub")
    # monitor = Monitoring("Cloud Monitoring")
    GCS=Storage("GCS" ,fontsize="16")
    bq=Bigquery("Bigquery" ,fontsize="16")


GCS >> bq
   
