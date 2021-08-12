import streamlit as st

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

def get_classifier(clf_name):
    
    param_expander = st.sidebar.beta_expander('Optional Parameter(s)')
    params = {}
    
    if clf_name == 'k-NN':
        n_neighbors = param_expander.slider('k', 1, 15)
        params['n_neighbors'] = n_neighbors
        
    elif clf_name == 'SVC':
        C = param_expander.slider('C', 0.01, 10.0)
        kernel = param_expander.selectbox(
            'Kernel',
            ('linear', 'poly', 'rbf', 'sigmoid'))
        params['C'] = C
        params['kernel'] = kernel
        
    elif clf_name == 'Perceptron':
        penalty = param_expander.selectbox(
            'Penalty',
            ('l1', 'l2', 'elasticnet', None))
        params['penalty'] = penalty
        
    elif clf_name == 'Decision Tree':
        criterion = param_expander.selectbox(
            'criterion',
            ('gini', 'entropy'))
        splitter = param_expander.selectbox(
            'splitter',
            ('best', 'random'))
        params['criterion'] = criterion
        params['splitter'] = splitter
        
    elif clf_name == 'Random Forest':
        n_estimators = param_expander.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators    
    
    return params

def get_model(clf_name):
    
    params = get_classifier(clf_name)
    clf = None
    
    if clf_name == 'k-NN':
        clf = KNeighborsClassifier(params['n_neighbors'])
        
    elif clf_name == 'SVC':
        clf = SVC(params['C'], params['kernel'])
        
    elif clf_name == 'Perceptron':
        clf = Perceptron(params['penalty'])
        
    elif clf_name == 'Decision Tree':
        clf = DecisionTreeClassifier(params['criterion'], params['splitter'])
        
    elif clf_name == 'Random Forest':
        clf = RandomForestClassifier(params['n_estimators'])
    
    return clf