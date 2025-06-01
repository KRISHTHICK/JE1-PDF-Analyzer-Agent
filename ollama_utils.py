# ollama_utils.py

import ollama

MODEL = "gemma"  # You can change this to "mistral" or any model you’ve pulled locally

def get_summary(text):
    prompt = f"Summarize the following document in simple terms:\n\n{text[:3000]}"
    response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def ask_question(context, question):
    prompt = f"Based on this document:\n\n{context[:3000]}\n\nAnswer this question: {question}"
    response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']
