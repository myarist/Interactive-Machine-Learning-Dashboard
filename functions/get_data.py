from functions.custom_dataset import *

import streamlit as st

from sklearn import datasets

@st.cache
def get_data(dataset_name):
    data = None
    
    if dataset_name == 'Iris':
        data = datasets.load_iris()
        X, y = data.data, data.target
    elif dataset_name == 'Cancer':
        data = datasets.load_breast_cancer()
        X, y = data.data, data.target
    elif dataset_name == 'Wine':
        data = datasets.load_wine()
        X, y = data.data, data.target
    elif dataset_name == 'Digits':
        data = datasets.load_digits()
        X, y = data.data, data.target
    elif dataset_name == 'XoR':
        X, y = get_xor()
    else:
        X, y = get_donut()
        
    return X, y