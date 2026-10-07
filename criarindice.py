import os

from pymilvus import DataType, MilvusClient

URI = os.getenv("ZILLIZ_URI")
TOKEN = os.getenv("ZILLIZ_TOKEN")

cliente = MilvusClient(
    uri=URI,
    token=TOKEN
)

index_params = cliente.prepare_index_params()

index_params.add_index( 
    field_name="embedding",
    index_type="AUTOINDEX",
    metric_type ="L2"
)

cliente.create_index(
    collection_name="Aluno",
    index_params=index_params
)