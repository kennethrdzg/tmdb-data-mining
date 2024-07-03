# Librerías
import os
import pandas as pd

from lib.cleaning import clean_data

if __name__=="__main__": 
    dataset = "top_10000_popular_movies_tmdb.csv"
    final_dataset = "popular_movies.csv"

    if not os.path.exists("../dataset/"+dataset): 
        print("No existe el dataset requerido")
        exit()
    
    clean_data(f'../dataset/{dataset}', f'../dataset/{final_dataset}')