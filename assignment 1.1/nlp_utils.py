import spacy
import nltk
from nltk.stem import PorterStemmer

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize NLTK stemmer
stemmer = PorterStemmer()

def tokenize(text):
    doc = nlp(text)
    return [token.text for token in doc]

def lemmatize(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc]

def stem(text):
    tokens = nltk.word_tokenize(text)
    return [stemmer.stem(token) for token in tokens]

def pos_tag(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

def ner(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def compare_lemmatization_stemming(text):
    lemmas = lemmatize(text)
    stems = stem(text)
    return list(zip(lemmas, stems)) 