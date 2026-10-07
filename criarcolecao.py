import os

from pymilvus import DataType, MilvusClient

URI = os.getenv("ZILLIZ_URI")
TOKEN = os.getenv("ZILLIZ_TOKEN")

cliente = MilvusClient(uri=URI,token=TOKEN)

print(cliente)
print(cliente.list_collections())

schema = cliente.create_schema()

schema.add_field(
    field_name="id",
    datatype=DataType.INT64,
    is_primary=True,
    auto_id=True
)

schema.add_field(
    field_name="texto",
    datatype=DataType.VARCHAR,
    max_length=500
)

schema.add_field(
    field_name="embedding",
    datatype=DataType.FLOAT_VECTOR,
    dim=768
)

cliente.create_collection(
    collection_name="Aluno",
    schema=schema,
    # index_params=index_params
)


print(cliente.list_collections())

