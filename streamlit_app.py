import streamlit as st
import pandas as pd
import gzip

st.title("🧬 Omics Feature Selection + Clustering App")

@st.cache_data
def load_data():
    with gzip.open("HiSeqV2.gz", "rt") as f:
        df = pd.read_csv(f, sep='\t', index_col=0)
    return df.T  # samples × genes

st.markdown("Loading TCGA-BRCA gene expression data...")
df = load_data()
st.write("Shape of expression matrix:", df.shape)
st.dataframe(df.iloc[:5, :5])

# Add UI for method selection (to be extended)
st.sidebar.header("Settings")
method = st.sidebar.selectbox("Feature Selection Method", ["Variance Threshold", "Random Forest", "LASSO"])
cluster = st.sidebar.selectbox("Clustering Method", ["K-Means", "Agglomerative", "DBSCAN"])

if st.button("Run Analysis"):
    st.success(f"Feature Selection: {method}, Clustering: {cluster} coming soon 🚀")
