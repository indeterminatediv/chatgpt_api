import streamlit as st
import openai
from apikey import APIKEY
openai.api_key = APIKEY

user_input = st.text_input("Enter a string:")

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": 
             user_input}]
)

# Print out the whole output dictionary
print(output)

# Get the output text only
#print(output['choices'][0]['message']['content'])
st.subheader(output['choices'][0]['message']['content'])