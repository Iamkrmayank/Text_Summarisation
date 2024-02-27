import streamlit as st

import os
import openai
from openai import OpenAI

st.title("Text generation Using AI")
client = OpenAI(api_key='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')

def Messages(query):
    response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=f"Summarize the text : {query}",
    temperature=0.7,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    #print(response)
    #if 'choices' in response:
        #if (len(response.choices)>0):
    answer = response.choices[0].text
    return answer
    #print(answer)

query = st.text_input("Enter something in prompt : ")

if st.button("Get response"):
  response = Messages(query)
  st.text("Model response")
  st.write(response)
