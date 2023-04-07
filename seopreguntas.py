import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import streamlit as st

def keyword_clustering(file, num_clusters):
    # Cargar el archivo CSV en un DataFrame de pandas
    data = pd.read_csv(file)

    # Crear una matriz de términos-documentos utilizando TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['text'])

    # Ejecutar KMeans para crear los clusters
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)

    # Agregar una columna al DataFrame que contenga el número de cluster asignado a cada fila
    data['cluster'] = kmeans.labels_

    return data

# Crear widgets para subir y descargar archivos
file = st.file_uploader('Upload CSV', type=['csv'])
download_button = st.button('Download CSV')

# Crear un widget para seleccionar el número de clusters
num_clusters = st.slider('Number of clusters', min_value=2, max_value=20, value=5)

# Ejecutar el clustering cuando se carga el archivo y se hace clic en el botón "Cluster"
if file is not None:
    data = keyword_clustering(file, num_clusters)
    st.write(data)

# Descargar el archivo cuando se hace clic en el botón "Download"
if download_button and data is not None:
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="clustered_data.csv">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
if __name__ == '__main__':
    st.set_page_config(page_title='Keyword Clustering Tool')
    st.title('Keyword Clustering Tool')
    st.write('Upload a CSV file and select the number of clusters to perform keyword clustering.')

    main()


