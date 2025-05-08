from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import spacy
import numpy as np
from sklearn.manifold import TSNE
from typing import List, Dict
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_md")
except OSError:
    raise RuntimeError("Please download the spaCy model using: python -m spacy download en_core_web_md")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.get("/api/embedding/{word}")
async def get_embedding(word: str):
    try:
        doc = nlp(word)
        if not doc.has_vector:
            raise HTTPException(status_code=404, detail="Word not found in vocabulary")
        return {"embedding": doc.vector.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/neighbors/{word}")
async def get_neighbors(word: str, n: int = 5):
    try:
        doc = nlp(word)
        if not doc.has_vector:
            raise HTTPException(status_code=404, detail="Word not found in vocabulary")
        
        # Get most similar words
        queries = [w for w in nlp.vocab if w.has_vector and w.is_lower and w.is_alpha]
        by_similarity = sorted(queries, key=lambda w: doc.similarity(w), reverse=True)
        neighbors = [{"word": w.text, "similarity": float(doc.similarity(w))} 
                    for w in by_similarity[1:n+1]]  # Skip the word itself
        return {"neighbors": neighbors}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/visualize")
async def visualize_words(words: List[str]):
    try:
        # Get embeddings for all words
        embeddings = []
        valid_words = []
        for word in words:
            doc = nlp(word)
            if doc.has_vector:
                embeddings.append(doc.vector)
                valid_words.append(word)
        
        if not embeddings:
            raise HTTPException(status_code=400, detail="No valid words found")
        
        # Convert to numpy array
        embeddings = np.array(embeddings)
        
        # Apply t-SNE
        tsne = TSNE(n_components=3, random_state=42, perplexity=4)
        reduced_embeddings = tsne.fit_transform(embeddings)
        
        # Prepare response
        result = {
            "words": valid_words,
            "coordinates": reduced_embeddings.tolist()
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 