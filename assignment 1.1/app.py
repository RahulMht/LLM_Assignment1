from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from nlp_utils import tokenize, lemmatize, stem, pos_tag, ner, compare_lemmatization_stemming

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TextInput(BaseModel):
    text: str

@app.post("/process")
async def process_text(input_data: TextInput):
    text = input_data.text
    return {
        "tokenization": tokenize(text),
        "lemmatization": lemmatize(text),
        "stemming": stem(text),
        "pos_tagging": pos_tag(text),
        "ner": ner(text)
    }

@app.post("/compare")
async def compare(input_data: TextInput):
    text = input_data.text
    return {"comparison": compare_lemmatization_stemming(text)} 