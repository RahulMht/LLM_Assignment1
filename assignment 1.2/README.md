# Word Embeddings Visualization

This project provides a web application for exploring word embeddings using GloVe vectors and visualizing them using t-SNE dimensionality reduction.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download spaCy model:
```bash
python -m spacy download en_core_web_md
```

4. Start the server:
```bash
uvicorn main:app --reload
```

5. Open your browser and navigate to `http://localhost:8000`

## Features

- Word embedding visualization using t-SNE
- Find nearest neighbors for input words
- Interactive 3D visualization
- REST API for embedding computation

## API Endpoints

- `GET /api/embedding/{word}`: Get embedding for a specific word
- `GET /api/neighbors/{word}`: Get nearest neighbors for a word
- `POST /api/visualize`: Get visualization data for multiple words 