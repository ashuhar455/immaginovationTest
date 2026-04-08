import os

DATA_PATH = "data/context.txt"

def load_context():
    if not os.path.exists(DATA_PATH):
        return ""
    with open(DATA_PATH, "r") as f:
        return f.read()

def retrieve_relevant_context(question: str) -> str:
    return load_context()
