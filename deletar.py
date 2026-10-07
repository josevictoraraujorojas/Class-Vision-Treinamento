import os

from pymilvus import DataType, MilvusClient

URI = os.getenv("ZILLIZ_URI")
TOKEN = os.getenv("ZILLIZ_TOKEN")

cliente = MilvusClient(
    uri=URI,
    token=TOKEN
)

cliente.delete(
    collection_name="Aluno",
    ids=[469253839548464594]
)