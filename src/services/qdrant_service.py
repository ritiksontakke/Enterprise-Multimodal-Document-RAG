from qdrant_client import QdrantClient


class QdrantService:

    client = QdrantClient(
        host="localhost",
        port=6333
    )