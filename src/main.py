# Librerías
import os
import pandas as pd

if __name__=="__main__": 
    dataset = "top_10000_popular_movies_tmdb.csv"

    if not os.path.exists("../dataset/"+dataset): 
        print("No existe el dataset requerido")
        exit()
