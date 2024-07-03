import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt
from os import path, mkdir

def classify(df: pd.DataFrame, showing = False): 
    if not path.exists('img'): 
        mkdir('img')
    if not path.exists('img/classifications'): 
        mkdir('img/classifications')

    result = df.drop(['title', 'release_date', 'genres', 'original_language', 'overview', 'production_companies', 'tagline'], axis=1)
    correlation_matrix = result.corr()

    X = result.drop('budget', axis=1).values
    y = result['budget'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345)
    knn_model = KNeighborsRegressor(n_neighbors=20)
    knn_model.fit(X_train, y_train)

    training_predictions = knn_model.predict(X_train)
    mse = mean_squared_error(y_train, training_predictions)
    rmse = sqrt(mse)

    test_predictions = knn_model.predict(X_test)
    mse = mean_squared_error(y_test, test_predictions)
    rmse = sqrt(mse)

    cmap = sns.cubehelix_palette(as_cmap=True)
    f, ax = plt.subplots()
    points = ax.scatter(X_test[:, 3], X_test[:, 4], c = test_predictions, s = 50, cmap=cmap)
    f.colorbar(points)
    
    if showing: 
        plt.show()
    else: 
        plt.savefig('img/classifications/test_prediction.png')
    plt.cla()

    cmap = sns.cubehelix_palette(as_cmap=True)
    f, ax = plt.subplots()
    points = ax.scatter(X_test[:, 3], X_test[:, 4], c=y_test, s=50, cmap=cmap)
    f.colorbar(points)

    if showing: 
        plt.show()
    else: 
        plt.savefig('img/classifications/y_test.png')