import streamlit as st
import requests
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from auth import verify_user

# Login sidebar (clearly)
st.sidebar.header("Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.sidebar.button("Login"):
    role = verify_user(username, password)
    if role:
        st.session_state['logged_in'] = True
        st.session_state['role'] = role
        st.sidebar.success(f"Logged in as {role}")
    else:
        st.sidebar.error("Incorrect username or password.")

# Main Chatbot UI (clearly after login)
if st.session_state.get('logged_in', False):
    st.title("FactoryTwin Analytics Chatbot")

    # Load Phi-2 clearly (Local)
    @st.cache_resource
    def load_phi2_model():
        model_path = "./models/phi-2"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
        return tokenizer, model

    tokenizer, model = load_phi2_model()

    query = st.text_input("Enter your analytics query:")

    if st.button("Get Insights"):
        # Call predictive analytics API (clearly and explicitly)
        try:
            api_response = requests.get("http://localhost:8000/predictive_inventory")
            analytics_response = api_response.json()['analytics']
        except:
            analytics_response = "No analytics data available. Ensure API is running."

        # Generate response explicitly using Phi-2
        input_prompt = f"Analytics Data: {analytics_response}\nQuestion: {query}\nAnswer:"
        inputs = tokenizer(input_prompt, return_tensors="pt", max_length=512, truncation=True)

        outputs = model.generate(inputs.input_ids, max_length=250, do_sample=True)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.write(response)

else:
    st.warning("Please login first.")
