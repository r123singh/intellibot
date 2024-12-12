import streamlit as st
# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("🦜🔗 Langchain - Blog Outline Generator")

openai_api_key = st.sidebar.text_input("Open API Key", type='password')

def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name = "gpt-3.5-turbo-instruct", openai_api_key = openai_api_key)
    # Prompt
    template = "As an experienced data scientist and writer, generate an outline for a blog about {topic}."
    prompt = PromptTemplate(input_variables=['topic'], template=template)
    prompt_query = prompt.format(topic = topic)
    # run the llm model
    response = llm(prompt_query)
    # print results
    return st.info(response)

with st.form('myForm'):
    topic_text= st.text_input('Enter prompt:', "")
    submitted = st.form_submit_button('Submit')
    if not openai_api_key:
        st.info('Please add your OpenAI API key to continue')
    elif submitted:
        blog_outline(topic_text)