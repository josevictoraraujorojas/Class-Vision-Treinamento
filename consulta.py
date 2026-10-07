import os

from pymilvus import DataType, MilvusClient

URI = os.getenv("ZILLIZ_URI")
TOKEN = os.getenv("ZILLIZ_TOKEN")

cliente = MilvusClient(
    uri=URI,
    token=TOKEN
)

cliente.load_collection("Aluno")

resultado = cliente.search(
    collection_name="Aluno",
    data=[[0.1] * 768], 
    anns_field="embedding",
    limit=5,
    filter='texto == "SI"',
    output_fields=["id", "texto"]
)

print(resultado)