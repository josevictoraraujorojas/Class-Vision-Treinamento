import os

from pymilvus import DataType, MilvusClient

URI = os.getenv("ZILLIZ_URI")
TOKEN = os.getenv("ZILLIZ_TOKEN")

cliente = MilvusClient(
    uri=URI,
    token=TOKEN
)

cliente.upsert(
    collection_name="Aluno",
    data=[
        {
            "id":  469253839548464384,
            "texto": "Aluno do 7º período de Sistemas de Informação",
            "embedding": [0.15] * 768
        }
    ]
)