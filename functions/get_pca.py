import streamlit as st

from sklearn.decomposition import PCA

@st.cache
def dimension_reduction(X):
    
    pca = PCA(2)

    if X.shape[1] > 3:
        X_red = pca.fit_transform(X)
    else:
        X_red = X
        
    return X_red