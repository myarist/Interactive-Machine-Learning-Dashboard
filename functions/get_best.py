from functions.get_classifier import *
from functions.get_plot import *

import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def get_best_classifier(X, y):
    
    accuracies = {}
    classifiers = ['k-NN', 'SVC', 'Perceptron', 'Decision Tree', 'Random Forest']
    
    for classifier in classifiers:
        
        clf = get_best_model(classifier)

        # Train Test Split

        X_train, X_test, y_train, y_test = train_test_split(\
            X, y, test_size=0.25, random_state=46)

        # Fit Data

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        # Metrics

        accuracies[classifier] = accuracy_score(y_test, y_pred)
    
    max_class = max(accuracies, key=accuracies.get)
    
    classifier_name = st.sidebar.selectbox(
        'Choose Classifier',
        ('None', 'k-NN', 'SVC', 'Perceptron', 'Decision Tree', 'Random Forest'),
        index=classifiers.index(max_class) + 1
    )
    
    return classifier_name

def get_best_model(clf_name):
    
    clf = None
    
    if clf_name == 'k-NN':
        clf = KNeighborsClassifier()
        
    elif clf_name == 'SVC':
        clf = SVC()
        
    elif clf_name == 'Perceptron':
        clf = Perceptron()
        
    elif clf_name == 'Decision Tree':
        clf = DecisionTreeClassifier()
        
    elif clf_name == 'Random Forest':
        clf = RandomForestClassifier()
    
    return clf

def get_best_result(classifier_name, X, y):
    
    clf = get_best_model(classifier_name)

    X_train, X_test, y_train, y_test = train_test_split(\
        X, y, test_size=0.25, random_state=46)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    st.markdown("<h3 style='text-align: center;'>\
        The Comparison Between Actual and Predicted Label</h3>", 
                unsafe_allow_html=True)

    col1, col2 = st.beta_columns(2)
        
    col1.markdown("<h4 style='text-align: center;'>Actual</h4>", 
                    unsafe_allow_html=True)
    col1.markdown('####')
    get_plot_data(X_test, y_test, col1, (5, 4))

    col2.markdown("<h4 style='text-align: center;'>Predicted</h4>", 
                    unsafe_allow_html=True)
    col2.markdown('####')
    get_plot_data(X_test, y_pred, col2, (5, 4))
    
    st.markdown(f"<h2 style='text-align: center;'>\
                    {'Accuracy : ' + str(acc)}</h2>", 
                unsafe_allow_html=True)