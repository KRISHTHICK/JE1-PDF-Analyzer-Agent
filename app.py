# File: app.py

import streamlit as st
from pdf_utils import extract_text_from_pdf
from ollama_utils import get_summary, ask_question

st.set_page_config(page_title="PDF LLM Agent", layout="wide")
st.title("📄 PDF Analyzer Agent with Local LLM")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    if pdf_text:
        st.subheader("📃 Extracted Text Preview:")
        st.text_area("PDF Content", pdf_text[:3000], height=300)

        if st.button("Summarize PDF"):
            with st.spinner("Summarizing using local LLM (via Ollama)..."):
                summary = get_summary(pdf_text)
            st.success("Summary Generated!")
            st.text_area("📌 Summary", summary, height=250)

        st.subheader("💬 Ask a Question about the PDF")
        user_question = st.text_input("Type your question")
        if st.button("Get Answer") and user_question:
            with st.spinner("Thinking..."):
                answer = ask_question(pdf_text, user_question)
            st.success("Answer:")
            st.write(answer)
    else:
        st.warning("Couldn't extract text from the uploaded PDF.")
else:
    st.info("Please upload a PDF to begin.")
