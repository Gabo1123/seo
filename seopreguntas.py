pip install streamlit pandas

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cluster Extractor")

# Upload CSV data
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    from sklearn.cluster import KMeans

# Extract clusters from data
kmeans = KMeans(n_clusters=3).fit(df)
df["Cluster"] = kmeans.labels_

# Show clusters in a pandas table
st.write(df)

# Allow user to download data as CSV
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="clusters.csv">Download CSV file</a>'
st.markdown(href, unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import base64
from sklearn.cluster import KMeans

st.set_page_config(page_title="Cluster Extractor")

# Upload CSV data
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Extract clusters from data
    kmeans = KMeans(n_clusters=3).fit(df)
    df["Cluster"] = kmeans.labels_

    # Show clusters in a pandas table
    st.write(df)

    # Allow user to download data as CSV
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="clusters.csv">Download CSV file</a>'
    st.markdown(href, unsafe_allow_html=True)

