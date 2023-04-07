import streamlit as st
from googlesearch import search

# Función para buscar preguntas en las SERPs de Google
def get_questions(keyword, num_results=20):
    query = f"intitle:preguntas {keyword} site:answers.yahoo.com"
    results = search(query, num_results=num_results)
    return results

# Configuración de la página de Streamlit
st.set_page_config(page_title="Extractor de Preguntas", layout="wide")

st.title("Extractor de Preguntas de Google SERP")

# Entrada de la keyword en la interfaz de Streamlit
keyword = st.text_input("Introduce la palabra clave:")

# Al hacer clic en el botón "Buscar", se ejecuta la función get_questions()
if st.button("Buscar"):
    if keyword:
        with st.spinner("Buscando preguntas..."):
            questions = get_questions(keyword)

        if questions:
            st.header("Preguntas encontradas:")
            for i, question in enumerate(questions, start=1):
                st.write(f"{i}. {question}")
        else:
            st.warning("No se encontraron preguntas relacionadas con la palabra clave ingresada.")
    else:
        st.warning("Por favor, ingresa una palabra clave para buscar.")
