# NLP Preprocessing Basics

This project demonstrates core NLP preprocessing techniques using spaCy and NLTK, exposed via a REST API and a simple web interface.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. Run the backend:
   ```bash
   uvicorn app:app --reload
   ```

4. Open `frontend/index.html` in your browser to use the web interface.

## Usage

- **Process Text**: Send a POST request to `/process` with a JSON body `{"text": "your text here"}` to get tokenization, lemmatization, stemming, POS tagging, and NER results.
- **Compare Lemmatization vs Stemming**: Send a POST request to `/compare` with a JSON body `{"text": "your text here"}` to see the comparison.

## Example

```bash
curl -X POST http://localhost:8000/process -H "Content-Type: application/json" -d '{"text": "The quick brown fox jumps over the lazy dog."}'
``` 