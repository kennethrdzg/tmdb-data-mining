# Librerías
import os
import pandas as pd

from lib.cleaning import clean_data
from lib.analysis import analyze
from lib.visualization import visualize

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

