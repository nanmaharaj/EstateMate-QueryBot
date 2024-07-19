import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.set_page_config(page_title="EstateMate", page_icon="🏠")


st.title("EstateMate")
st.markdown("*Ask questions about properties!*")


question = st.text_input("Ask a question:", key="question_input")


st.markdown("---")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)


    st.header("Answer")
    st.info(response)

st.markdown("---")
st.markdown("Built by HNR")
