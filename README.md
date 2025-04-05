# Text_Clustering_project
 20 Newsgroups Dataset

**Description**:  
A classic dataset of ~20,000 newsgroup documents organized into 20 categories, covering diverse topics.

**Source**:  
[20 Newsgroups Dataset - UCI Repository](https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups)

**Features**:
- **Content**: Post body text
- **Headers**: Metadata (subject, author, date)
1. **Data Collection**  
   - Download datasets from the respective sources.

2. **Data Preprocessing**  
   - Text cleaning (lowercasing, stemming, etc.)  
   - Tokenization  
   - Stop word removal

3. **Feature Extraction**  
   - TF-IDF Vectorization  
   - (Optional) Word embeddings like Word2Vec or GloVe

4. **Clustering Algorithms**  
   - K-Means  
   - Hierarchical Clustering
5. **Evaluation**  
   - Silhouette Score  
   - Purity Score

6. **Visualization**  
   - t-SNE / PCA
   - Dendrograms
   - **Language**: Python  
- **Libraries**:  
  - `pandas`, `NumPy`  
  - `NLTK`, `spaCy`  
  - `scikit-learn`, `gensim`  
  - `matplotlib`, `seaborn`
