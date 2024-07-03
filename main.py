# Librerías
import os
import pandas as pd

from lib.cleaning import clean_data
from lib.analysis import analyze
from lib.visualization import visualize
from lib.statistic_test import stat_test
from lib.linear_regression import get_linear_regression
from lib.forecasting import forecast
from lib.classification import classify
from lib.clustering import cluster

if __name__=="__main__": 
    dataset = "top_10000_popular_movies_tmdb.csv"
    final_dataset = "popular_movies.csv"

    if not os.path.exists("dataset/"+dataset): 
        print("No existe el dataset requerido")
        exit()

    df: pd.DataFrame = None

    if os.path.exists(f'dataset/{final_dataset}'): 
        df = pd.read_csv(f'dataset/{final_dataset}')
    else: 
        print("Limpieza de datos")    
        df = clean_data(f'dataset/{dataset}', f'dataset/{final_dataset}')
        print("-"*40)

    print("Análisis de Datos:")
    analyze(df)
    print("-"*40)

    print("Visualización:")
    visualize(df)
    print("-"*40)

    print("Tabla ANOVA")
    stat_test(df)
    print("-"*40)

    print("Regresión lineal")
    get_linear_regression(df)

    print("Predicción")
    forecast(df)

    print("Clasificación")
    classify(df)
    print("Clustering")
    cluster(df)