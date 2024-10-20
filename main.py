# pip install langchain
# pip install streamlit
# pip install langchain_community
# !pip install huggingface_hub
import streamlit as st
from langchain import HuggingFaceHub, LLMChain
from langchain_core.prompts import PromptTemplate
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

hub_llm = HuggingFaceHub(
    huggingfacehub_api_token= os.environ['HUGGINGFACEHUB_API_TOKEN'],
    repo_id='google/pegasus-xsum',
    model_kwargs={"temperature": 0.5, "max_length": 100, "min_length" : 10}
)


template = """ You are a helpful AI assistant who summarizes given paragaraphs as inputs properly and do not give
any false information just for the sake of answering.You give complete summarized answer which is ended properly

Question: {query}

Answer:
"""

prompt = PromptTemplate(template=template, input_variables=["query"])

llm_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm
)
def main():
    st.title("Summarizer")
    query = st.text_input("Enter you Paragraph to be summarized")
    if st.button("Submit"):
        result = llm_chain.run(query)
        st.success(result)

if __name__ == "__main__":
    main()    