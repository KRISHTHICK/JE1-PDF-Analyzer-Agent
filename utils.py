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
