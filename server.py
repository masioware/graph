from gremlin_python.driver.client import Client
from gremlin_python.driver.serializer import GraphSONSerializersV3d0

URL = 'ws://localhost:8182/gremlin'


def gremlin():
    return Client(URL, 'g', message_serializer=GraphSONSerializersV3d0())


client = gremlin()


def execute(query: str):
    return client.submitAsync(query).result().all()


def execute_batch(queries: list):
    for query in queries:
        yield execute(query)
