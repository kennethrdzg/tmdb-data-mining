from os import path, mkdir
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def regress_line(df: pd.DataFrame, x_axis: str, y_axis: str, agg_func = '', showing = False): 
    img_path = "img/linear_regressions"
    if not path.exists('img'): 
        mkdir('img')
    if not path.exists(img_path): 
        mkdir(img_path)

    if agg_func != '': 
        result = df.groupby(x_axis)[y_axis].aggregate(agg_func)

        X = np.array(result.keys()).reshape(-1, 1)
        Y = np.array(result.values).reshape(-1, 1)
    else: 
        X = np.array(df[x_axis].values).reshape(-1, 1)
        Y = np.array(df[y_axis].values).reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    plt.cla()
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.xlabel(xlabel=x_axis.upper())
    plt.ylabel(ylabel=y_axis.upper())
    plt.title(label=x_axis.upper() + " vs. " + y_axis.upper())
    if showing: 
        plt.show()
    else: 
        plt.savefig(f'{img_path}/{x_axis.lower()}_vs_{y_axis.lower()}.png')

def get_linear_regression(dataset: str, showing = False): 
    df: pd.DataFrame = pd.read_csv(dataset)
    if not showing: 
        print("Generando gráficas...")
    regress_line(df, x_axis='release_year', y_axis='id', agg_func='count', showing=showing)
    regress_line(df, x_axis='release_year', y_axis='budget', agg_func='mean', showing=showing)
    regress_line(df, x_axis='release_year', y_axis='revenue', agg_func='mean', showing=showing)
    regress_line(df, x_axis='release_year', y_axis='runtime', agg_func='mean', showing=showing)
    regress_line(df, x_axis='budget', y_axis='revenue', showing=showing)
    regress_line(df, x_axis='runtime', y_axis='revenue', showing=showing)
    regress_line(df, x_axis='budget', y_axis='popularity', showing=showing)
    regress_line(df, x_axis='budget', y_axis='vote_average', showing=showing)
    regress_line(df, x_axis='vote_average', y_axis='popularity', showing=showing)
    if not showing: 
        print("Gráficas generadas con éxito en img/linear_regressions.")