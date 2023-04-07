import requests
from bs4 import BeautifulSoup
import streamlit as st

st.title("Extractor de Preguntas de Bing")

# Entrada de la palabra clave
keyword = st.text_input("Ingresa la palabra clave:")

# Palabras clave de las preguntas
question_words = ["cómo", "cuándo", "dónde", "por qué", "para qué"]

def fetch_search_results(keyword, count=20):
    url = f"https://www.bing.com/search?q={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("li", class_="b_algo")

    questions = []
    for result in search_results:
        title = result.find("a").text
        for word in question_words:
            if word in title.lower():
                questions.append(title)
                break
    return questions[:count]

if keyword:
    questions = fetch_search_results(keyword)
    if questions:
        st.subheader("Preguntas encontradas:")
        for question in questions:
            st.write(question)
    else:
        st.write("No se encontraron preguntas relacionadas con la palabra clave.")
