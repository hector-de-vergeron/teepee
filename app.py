# app.py
import streamlit as st
from langflow import load_flow_from_json

# Chargement du chatbot une seule fois
@st.cache_resource
def load_chatbot():
    return load_flow_from_json("ton_flow.json")

flow = load_chatbot()

st.title("🤖 Chat avec mon chatbot Langflow")
st.write("Pose-lui une question !")

# Zone de texte pour entrer la question
user_input = st.text_input("Vous :", "")

# Si l'utilisateur écrit quelque chose
if user_input:
    with st.spinner("Le bot réfléchit..."):
        response = flow(user_input)
    st.markdown(f"**Bot** : {response}")
