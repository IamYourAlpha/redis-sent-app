import streamlit as st
import requests
from cache import retrieve, addToCache

# http://docker_container_name:exposed_port/predicts
FASTAPI_URL = "http://web-app:8000/predict"
# FASTAPI_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Sentence Similarity", layout="centered")

st.title("🔍 Sentence Similarity")

str1 = st.text_input("Enter Sentence 1:")
str2 = st.text_input("Enter Sentence 2:")
result_global = 10
if st.button("Compute Similarity") and str1 and str2:
    payload = {"str1": str1, "str2": str2}
    try:
        response = requests.post(FASTAPI_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Similarity Score: **{result[0]:.4f}**")
            result_global = result
    except Exception as e:
        st.error(f"Request failed: {e}")

st.markdown("---")

if st.button("add to cache"):
    try:
        addToCache(str1, str2, result)
    except Exception as e:
        st.error(f"Can not push to cache: {e}")
        # c1, c2, score
if st.button("Show Query History from Redis"):
    try:
        history = retrieve()
        if not history:
            st.info("No history found.")
        else:
            for entry in history:
                st.markdown(f"- **{entry['c1']}** ↔ **{entry['c2']}** → Score: `{entry['score']}`")
    except Exception as e:
        st.error(f"Failed to retrieve history: {e}")
