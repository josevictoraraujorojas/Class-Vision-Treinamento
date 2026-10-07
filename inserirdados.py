import os

from pymilvus import DataType, MilvusClient

URI = os.getenv("ZILLIZ_URI")
TOKEN = os.getenv("ZILLIZ_TOKEN")

cliente = MilvusClient(
    uri=URI,
    token=TOKEN
)

print(cliente.list_collections())

# Inserir
data = [{
    "texto": "SI",
    "embedding": [0.2] * 768
}]

resultado = cliente.insert(
    collection_name="Aluno",
    data=data
)

print("Inserção:")
print(resultado)

