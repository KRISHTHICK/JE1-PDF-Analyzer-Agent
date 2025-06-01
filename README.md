# JE1-PDF-Analyzer-Agent
GenAI

Great! Here's the complete code structure for your **PDF Analyzer Agent using Python, Streamlit, and Ollama**. We'll start with `app.py` — the main Streamlit application. Now let me provide the rest of the modules (`pdf_utils.py`, `ollama_utils.py`, and `requirements.txt`) and the explanation.

---

### 📄 **File: `pdf_utils.py`** (PDF text extraction)

```python
# pdf_utils.py

import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text.strip()
    except Exception as e:
        print("Error reading PDF:", e)
        return ""
```

---

### 🧠 **File: `ollama_utils.py`** (Local LLM interaction)

```python
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
```

---

### 📦 **File: `requirements.txt`**

```txt
streamlit
PyMuPDF
ollama
```

---

### 📘 **File: `README.md`** (for GitHub)

````markdown
# PDF Analyzer Agent with Local LLM 🧠📄

An AI-powered tool built with Streamlit, Python, and Ollama to:
- Extract text from PDFs
- Summarize them using a local LLM (Gemma, Mistral, etc.)
- Answer questions about the document content

## ⚙️ Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
````

2. Start Ollama and pull a model:

```bash
ollama run gemma
```

3. Run the app:

```bash
streamlit run app.py
```

> **Note**: No paid APIs or virtual environment (`venv`) required. Fully local!

## 🧠 Example Local Models:

* `gemma`
* `mistral`
* `llama2` (if you have enough memory)

---

## 📌 Features

* ✅ PDF Upload
* ✅ Text Extraction
* ✅ LLM-based Summarization
* ✅ Ask Questions About PDF

---

## 🔐 License

MIT

````

---

### ✅ How to Test

1. Install Ollama: https://ollama.com/download
2. Pull the model:
   ```bash
   ollama pull gemma
````

3. Run `streamlit run app.py`

---

Would you like me to also:

* Package this as a `.zip` for upload?
* Add multi-language support?
* Include PDF section-level summaries?

Let me know!
