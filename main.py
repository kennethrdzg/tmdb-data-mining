# Librerías
import os
import pandas as pd

from lib.cleaning import clean_data
from lib.analysis import analyze
from lib.visualization import visualize
from lib.statistic_test import stat_test
from lib.linear_regression import get_linear_regression
from lib.forecasting import forecast

if __name__=="__main__": 
    dataset = "top_10000_popular_movies_tmdb.csv"
    final_dataset = "popular_movies.csv"

    if not os.path.exists("dataset/"+dataset): 
        print("No existe el dataset requerido")
        exit()

    print("Limpieza de datos")    
    clean_data(f'dataset/{dataset}', f'dataset/{final_dataset}')
    print("-"*40)

    print("Análisis de Datos:")
    analyze(f'dataset/{final_dataset}')
    print("-"*40)

    print("Visualización:")
    visualize(f'dataset/{final_dataset}', False)
    print("-"*40)

    print("Tabla ANOVA")
    stat_test(f'dataset/{final_dataset}')
    print("-"*40)

    print("Regresión lineal")
    get_linear_regression(f'dataset/{final_dataset}')

    print("Predicción")
    forecast(f'dataset/{final_dataset}')