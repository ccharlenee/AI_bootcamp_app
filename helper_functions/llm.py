import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken

OPENAI_KEY = st.secrets["OPENAI_API_KEY"]
   
# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=OPENAI_KEY)


def get_embedding(input_text, model='text-embedding-3-small'):
    response = client.embeddings.create(
        input=input_text,
        model=model
    )
    return [x.embedding for x in response.data]


# This is the "Updated" helper function for calling LLM
def get_completion(prompt, model="gpt-4o-mini", temperature=0, top_p=1.0, max_tokens=1024, n=1, json_output=False):
    messages = [{"role": "user", "content": prompt}]
    output_json_structure = {"type": "json_object"} if json_output else None
    
    response = client.chat.completions.create( #originally was openai.chat.completions
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1,
        response_format=output_json_structure,
    )
    return response.choices[0].message.content


# Note that this function directly take in "messages" as the parameter.
def get_completion_by_messages(messages, model="gpt-4o-mini", temperature=0, top_p=1.0, max_tokens=1024, n=1):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=n
    )
    return response.choices[0].message.content


# This function is for calculating the tokens given the "message"
# ⚠️ This is simplified implementation that is good enough for a rough estimation
def count_tokens(text):
    encoding = tiktoken.encoding_for_model('gpt-4o-mini')
    return len(encoding.encode(text))


def count_tokens_from_message(messages):
    encoding = tiktoken.encoding_for_model('gpt-4o-mini')
    combined_text = ' '.join([x.get('content') for x in messages])
    return len(encoding.encode(combined_text))
