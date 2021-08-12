from functions.get_sidebar import *

import numpy as np
import pandas as pd
import streamlit as st

def main():
    
    st.set_page_config(page_title='Interactive ML Dashboard', page_icon = 'images/ml.ico')
    
    ########### Sidebar ###########
    
    st.sidebar.subheader('Dataset')
    data_upload = st.sidebar.file_uploader("Upload a Clean Dataset", type=("csv"))
    
    if data_upload:
        df = pd.read_csv(data_upload)
        
        if df.shape[1] < 3:
            st.sidebar.warning('Please Use Other Data with at Least\
                               3 Columns (2 Features and 1 Label)')
            
        else:
            upload_expander = st.sidebar.beta_expander('Choose the Feature and Label')

            X_col = upload_expander.multiselect('Feature(s)', df.columns.tolist())
            y_col = upload_expander.multiselect('Label(s)', df.columns.tolist())
            X_upload = np.array(df[X_col])
            y_upload = np.array(df[y_col])
    
    dataset_name = st.sidebar.selectbox(
        'Or Choose Predefined Dataset',
        ('None', 'Iris', 'Cancer', 'Wine', 'Digits', 'XoR', 'Donut'),
        index=0)
        
    ########### DOUBLE ###########
        
    if data_upload is not None and dataset_name != 'None':
        st.sidebar.warning('Please Choose Only One Dataset')

    ########### Data Upload ###########
    
    elif data_upload is not None and df.shape[1] >= 3:
        dataset_name = data_upload.name[:-4].title()
        empty = np.empty([0], dtype='float64')
        
        if X_col != empty and y_col != empty:
            get_sidebar_xy(dataset_name, X_upload, y_upload)
            
        else:
            upload_expander.warning('Choose the Feature and Label')
        
    ########### Data Predefined ###########
    
    elif dataset_name != 'None':
        get_sidebar(dataset_name)
    
    ########### Home ###########
    
    else:
        st.markdown("""
                    <h1 style='text-align: center;'>\
                        Interactive Machine Learning Dashboard</h1>
                    """, 
                    unsafe_allow_html=True)
        
        st.image('https://images.ctfassets.net/2yr4wv2jga4w/MqgSqW9FAcMqYG8mc0CSm/9427eedd4eea3c74b14e86357ce74791/data-revenue.gif', 
                 width=650)
        
        st.markdown("<h2 style='text-align: center;'>Project by <a href=\
                    'https://www.linkedin.com/in/myarist/' style=\
                        'text-decoration: none; color:white;'>\
                            Muhammad Yusuf Aristyanto</a></h2>", 
                    unsafe_allow_html=True)
        
if __name__ == '__main__':
    main()