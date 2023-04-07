import streamlit as st
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re

st.title('Extractor de preguntas relacionadas de Google SERP')
keyword = st.text_input('Introduce una palabra clave:', '')

def get_related_questions(query):
    questions = []
    query = query + " intitle:inurl:es.answers.yahoo.com"
    for j in search(query, num_results=20, lang='es'):
        try:
            page = requests.get(j)
            soup = BeautifulSoup(page.content, 'html.parser')
            question = soup.find('title').get_text(strip=True)
            question = re.sub(' \| Yahoo Respuestas$', '', question)
            questions.append(question)
        except Exception as e:
            print("Error:", e)
    return questions

if keyword:
    questions = get_related_questions(keyword)
    if questions:
        st.write('Preguntas relacionadas encontradas:')
        for i, question in enumerate(questions, 1):
            st.write(f'{i}. {question}')
    else:
        st.write('No se encontraron preguntas relacionadas.')
