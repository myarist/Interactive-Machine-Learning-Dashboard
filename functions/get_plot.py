from functions.get_pca import *

import matplotlib.pyplot as plt

def get_plot_data(X, y, loc, size=(5, 3)):
    
    X_red = dimension_reduction(X)
    
    fig = plt.figure(figsize=size)
    plt.style.use('dark_background')
    plt.scatter(X_red[:,0], X_red[:,1], c=y, alpha=0.8, cmap='viridis')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar()
    
    loc.pyplot(fig)