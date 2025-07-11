import streamlit as st
import pandas as pd
import gzip
import urllib.request

@st.cache_data
def load_remote_data():
    # Load expression data
    url_expr = "https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HiSeqV2.gz"
    with urllib.request.urlopen(url_expr) as response:
        with gzip.open(response, "rt") as f:
            df_expr = pd.read_csv(f, sep='\t', index_col=0).T  # samples x genes

    # Load sample type metadata
    url_meta = "https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/BRCA_clinicalMatrix"
    df_meta = pd.read_csv(url_meta, sep="\t", index_col=0)

    # Extract and align sample_type
    df_expr["sample_type"] = df_meta["sample_type"].reindex(df_expr.index)

    return df_expr


st.title("🧬 Omics Feature Selection + Clustering App")
df = load_remote_data()
st.write("Expression matrix shape:", df.shape)
st.dataframe(df.iloc[5:15, 10:20])
