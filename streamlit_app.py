import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
file=st.file_uploader('Pick a file')

if file is not None:
    loader = PyMuPDFLoader(file)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500
    )
    docs_split = text_splitter.split_documents(documents)

    st.write(docs_split[0])
    st.write(f'{len(documents)} documents have been splitted into {len(docs_split)} chunks')
