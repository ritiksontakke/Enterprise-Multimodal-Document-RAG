from fastapi import APIRouter, UploadFile, File
import os
from src.services.pdf_parser import PDFParser
from src.services.chunk_service import ChunkService
from src.services.embedding_service import EmbeddingService
from src.services.qdrant_service import QdrantService
router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    # Extract PDF Text
    text = PDFParser.extract_text(file_path)

    # Chunking
    chunks = ChunkService.create_chunks(text)
    first_chunk = chunks[0]

    vector = EmbeddingService.generate_embedding(text)
    embedding = EmbeddingService.generate_embedding(first_chunk)

    collections = QdrantService.client.get_collections()
    print(collections)



    return {
        "filename": file.filename,
        "text": text,
        "chunks": chunks,
        "vector" : vector,
        "embedding" :embedding

    }


    # return {
    #     "filename": file.filename,
    #     "total_chunks": len(chunks),
    #     "embedding_dimension": len(embedding)
    # }


    