from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingService:

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    @classmethod
    def generate_embedding(cls, text: str):
        return cls.embeddings.embed_query(text)