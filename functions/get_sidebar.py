from functions.get_best import *
from functions.get_data import *
from functions.get_result import *

import streamlit as st

def get_sidebar(dataset_name):

    X, y = get_data(dataset_name)

    st.sidebar.subheader('Classifier')
    best_button = st.sidebar.button('Find the Best Classifier Automatically ')
    
    if best_button:
        classifier_name = get_best_classifier(X, y)
        
        if classifier_name == 'None':
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset'}</h1>", 
                        unsafe_allow_html=True)

        else:
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset' + ' using ' + classifier_name}</h1>", 
                        unsafe_allow_html=True)
    
            get_best_result(classifier_name, X, y)
    
    else:
        classifier_name = st.sidebar.selectbox(
            'Or Choose Classifier Manually',
            ('None', 'k-NN', 'SVC', 'Perceptron', 'Decision Tree', 'Random Forest'),
            index=0)
        
        if classifier_name == 'None':
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset'}</h1>", 
                        unsafe_allow_html=True)
            get_plot_data(X, y, st, (5, 3))
            
        elif classifier_name != 'None':
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset' + ' using ' + classifier_name}</h1>", 
                        unsafe_allow_html=True)
            
            get_result(classifier_name, X, y)
            
def get_sidebar_xy(dataset_name, X, y):

    st.sidebar.subheader('Classifier')
    best_button = st.sidebar.button('Find the Best Classifier Automatically ')
    
    if best_button:
        classifier_name = get_best_classifier(X, y)
        
        if classifier_name == 'None':
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset'}</h1>", 
                        unsafe_allow_html=True)
            
        else:
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset' + ' using ' + classifier_name}</h1>", 
                        unsafe_allow_html=True)
            
            get_best_result(classifier_name, X, y)
    
    else:
        classifier_name = st.sidebar.selectbox(
            'Or Choose Classifier Manually',
            ('None', 'k-NN', 'SVC', 'Perceptron', 'Decision Tree', 'Random Forest'),
            index=0)
        
        if classifier_name == 'None':
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset'}</h1>", 
                        unsafe_allow_html=True)
            get_plot_data(X, y, st, (5, 3))

        elif classifier_name != 'None':
            st.markdown(f"<h1 style='text-align: center;'>\
                            {dataset_name + ' Dataset' + ' using ' + classifier_name}</h1>", 
                        unsafe_allow_html=True)
            
            get_result(classifier_name, X, y)