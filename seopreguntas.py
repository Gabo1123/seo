import streamlit as st
from googleapiclient.discovery import build
import re

# Reemplaza YOUR_API_KEY con tu clave de API
API_KEY = "YOUR_API_KEY"
SEARCH_ENGINE_ID = "012345678901234567890:abcdefghijklm"

# Función para extraer preguntas de los resultados de búsqueda
def extract_questions(query, num_results=20):
    questions = []
    service = build("customsearch", "v1", developerKey=API_KEY)
    response = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=num_results).execute()
    
    for item in response.get("items", []):
        title = item["title"]
        if re.search("(?i)(cómo|cuándo|dónde|por qué|para qué|cuál|quiénes|qué)", title):
            questions.append(title)
    return questions

# Aplicación Streamlit
st.title("Extractor de Preguntas de Google SERPs")
keyword = st.text_input("Ingresa la palabra clave:")
num_results = st.number_input("Número de resultados a considerar (máx. 100):", min_value=20, max_value=100, value=20)

if keyword:
    query = f"{keyword} intitle:(cómo OR cuándo OR dónde OR por qué OR para qué OR cuál OR quiénes OR qué)"
    questions = extract_questions(query, num_results)
    if questions:
        st.header("Preguntas encontradas:")
        for question in questions:
            st.write(question)
    else:
        st.warning("No se encontraron preguntas relacionadas con la palabra clave.")
