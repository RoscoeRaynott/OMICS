import streamlit as st
import pandas as pd
import gzip
import urllib.request

@st.cache_data
def load_remote_data():
    url = "https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HiSeqV2.gz"
    response = urllib.request.urlopen(url)
    with gzip.open(response, "rt") as f:
        df = pd.read_csv(f, sep='\t', index_col=0)
    return df.T

st.title("🧬 Omics Feature Selection + Clustering App")
df = load_remote_data()
st.write("Expression matrix shape:", df.shape)
st.dataframe(df.iloc[5:15, 10:20])
