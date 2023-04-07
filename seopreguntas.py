import streamlit as st
from googlesearch import search
import re

# Función para extraer preguntas de los resultados de búsqueda
def extract_questions(query, num_results=20):
    questions = []
    for j in search(query, num_results=num_results):
        title = j["title"]
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
