import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
file=st.file_uploader('Pick a file')

from langchain.document_loaders import PyMuPDFLoader
loader=PyMuPDFLoader(file)
documents=loader.load()

from langchain.text_splitter import CharacterTextSplitter

text_splitter=CharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500
)
docs_split=text_splitter.split_documents(documents)
print(docs_split[0])
print(f'{len(documents)} documents have been splitted into{len(docs_split)} chunks')
