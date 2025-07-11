import streamlit as st
import pandas as pd
import gzip
import urllib.request
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import io # New import

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

def plot_pca(df, label_column="sample_type"):
    features = df.drop(columns=[label_column])
    labels = df[label_column]

    pca = PCA(n_components=2)
    pcs = pca.fit_transform(features)

    pca_df = pd.DataFrame({
        "PC1": pcs[:, 0],
        "PC2": pcs[:, 1],
        "Label": labels
    })

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="Label", palette="Set1", alpha=0.7, s=50, ax=ax)
    ax.set_title("PCA: Colored by Sample Type")
    ax.legend(loc="best", title="Sample Type", bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    st.pyplot(fig)


st.title("🧬 Omics Feature Selection + Clustering App")
df = load_remote_data()
st.write("Expression matrix shape:", df.shape)
st.dataframe(df.iloc[5:15, 10:20])

st.subheader("PCA Visualization of Classes")
plot_pca(df, label_column="sample_type")


# --- Start of New Section ---

st.subheader("Download App Context")

# List of files to include in the download.
# To add more files, just add their filenames to this list.
files_to_include = ['app.py', 'requirements.txt'] # Assuming your script is named app.py

# Create an in-memory text buffer
context_buffer = io.StringIO()

for filename in files_to_include:
    context_buffer.write(f"--- Start of {filename} ---\n\n")
    try:
        with open(filename, 'r') as f:
            context_buffer.write(f.read())
        context_buffer.write(f"\n\n--- End of {filename} ---\n\n")
    except FileNotFoundError:
        st.warning(f"Warning: Could not find the file '{filename}'. It will not be included in the download.")


# Create the download button
st.download_button(
   label="Download context.txt",
   data=context_buffer.getvalue(),
   file_name="context.txt",
   mime="text/plain",
)

# --- End of New Section ---
