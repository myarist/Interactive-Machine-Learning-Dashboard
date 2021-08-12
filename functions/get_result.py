from functions.get_classifier import *
from functions.get_plot import *

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def get_result(classifier_name, X, y):

    X_train, X_test, y_train, y_test = train_test_split(\
        X, y, test_size=0.25, random_state=46)

    clf = get_model(classifier_name)
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