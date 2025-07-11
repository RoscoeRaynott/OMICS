# Omics Feature Selection and Clustering App

## 🧬 Dataset Description: TCGA-BRCA Gene Expression (HiSeqV2)

This project uses the publicly available gene expression dataset from **The Cancer Genome Atlas (TCGA)**, specifically the **Breast Invasive Carcinoma (BRCA)** cohort. The data is obtained from the **UCSC Xena browser**, which provides normalized and log-transformed RNA-seq gene expression data.

### 📦 Dataset Source:

* **URL**: [https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HiSeqV2.gz](https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HiSeqV2.gz)
* **Format**: Gzipped TSV file (`HiSeqV2.gz`)
* **Dimensions**: \~1,093 samples × \~20,500 genes
* **Data Type**: Log2(RSEM normalized count + 1) expression values
* **Sample Types**: Includes primary tumor and normal tissue samples

### 🧪 Preprocessing Status:

* Already normalized and log-transformed
* No missing values
* Sample identifiers follow TCGA barcode format
* Ideal for direct use in machine learning pipelines

## 📊 Project Objective

The goal of this project is to build an interactive **Streamlit app** that enables users to:

1. **Select features** (genes) using various statistical and machine learning methods
2. **Cluster samples** based on selected features
3. **Visualize the results** using PCA, UMAP, and heatmaps

The app will be deployed via **Streamlit Community Cloud**, allowing fully web-based exploration with no local setup required.

## 🚧 Development Plan (To Be Updated)

* [x] Dataset loading from URL
* [ ] Feature selection module
* [ ] Clustering methods integration (k-means, DBSCAN, etc.)
* [ ] Dimensionality reduction (PCA, UMAP)
* [ ] Visualization components

> This README will be updated as the project progresses. Stay tuned!
