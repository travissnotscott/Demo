#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

os.environ["REPLICATE_API_TOKEN"] = "r8_MFcqXyKNyootlhPQoa6zmGxPQVSv37m2nfGZo"


# In[16]:


import replicate

# Prompts
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "what is the function of water bottle?"

# Generate LLM response
output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                        input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters


# In[17]:


full_response = ""

for item in output:
  full_response += item

print(full_response)


# In[18]:


import streamlit as st


# In[19]:


# Streamlit UI setup
st.title("LLM Prompt Generator")
st.write("Enter a prompt and get a response from the language model.")

# Input prompt
prompt_input = st.text_area("Prompt", placeholder="Enter your question or command here...")

# Button to submit the prompt
if st.button("Generate Response"):
    if prompt_input.strip():
        with st.spinner("Generating response..."):
            response = generate_response(prompt_input)
        st.subheader("Response")
        st.write(response)
    else:
        st.warning("Please enter a valid prompt.")


# In[ ]:




