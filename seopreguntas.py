import requests
from bs4 import BeautifulSoup

def buscar_preguntas(keyword):
    # Realizar una búsqueda en Google para la palabra clave
    url = f"https://www.google.com/search?q={keyword}&hl=en"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    # Analizar el HTML de la página de resultados
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar los elementos HTML que contienen preguntas
    preguntas = []
    for element in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
        if element.text:
            preguntas.append(element.text)
    
    # Devolver una lista de preguntas encontradas
    return preguntas
