import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_questions(keyword):
    # Crear la URL de la búsqueda en Bing
    url = 'https://www.bing.com/search?q=' + keyword.replace(' ', '+') + '&qs=n&form=QBRE&sp=-1&pq=&sc=0-0&sk=&cvid='

    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Analizar el HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos los elementos de pregunta en la página
    question_elements = soup.find_all('h2', {'class': 'questionText'})

    # Crear una lista de preguntas a partir de los elementos encontrados
    questions = [element.text for element in question_elements]

    # Limitar la lista de preguntas a los primeros 20 elementos
    questions = questions[:20]

    # Devolver la lista de preguntas
    return questions

# Configurar la página de Streamlit
st.set_page_config(page_title='Bing Questions Extractor', page_icon=':memo:', layout='wide')

# Crear la barra lateral
st.sidebar.title('Bing Questions Extractor')
keyword = st.sidebar.text_input('Introduzca una palabra clave', value='Python')
if st.sidebar.button('Buscar en Bing'):
    questions = get_questions(keyword)
    st.write('Estas son las preguntas encontradas en Bing:')
    for question in questions:
        st.write('- ' + question)
