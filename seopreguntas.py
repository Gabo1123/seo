import streamlit as st
from googlesearch import search

st.set_page_config(page_title="SERP Preguntas", layout="wide")
st.title("Extractor de preguntas de SERPs")

# Función para extraer las preguntas de las SERPs
def get_questions(keyword):
    query = f"preguntas sobre {keyword}"
    questions = []

    for j in search(query, num_results=50):
        if j.startswith("https://www.quora.com/") or j.startswith("https://espanol.answers.yahoo.com/") or j.startswith("https://www.reddit.com/"):
            questions.append(j)
    
    return questions

# Creación de la interfaz de usuario
keyword = st.text_input("Introduce una palabra clave:")
submit_button = st.button("Buscar preguntas")

if submit_button:
    if keyword:
        st.write(f"Buscando preguntas relacionadas con '{keyword}' en las SERPs...")

        questions = get_questions(keyword)

        if questions:
            st.write(f"Preguntas encontradas:")

            for question in questions:
                st.write(question)
        else:
            st.write("No se encontraron preguntas relacionadas con la palabra clave.")
    else:
        st.write("Por favor, introduce una palabra clave.")
