import os
import pandas as pd
import matplotlib.pyplot as plt

def graph_output(img_path: str, showing = True): 
    if showing: 
        plt.show()
    else: 
        plt.savefig(img_path)

def visualize(dataset, showing = True): 
    img_path = '../img/graphs'
    if not os.path.exists("../img"): 
        os.mkdir("../img")
    elif not os.path.exists("../img/graphs"): 
        os.mkdir("../img/graphs")

    df: pd.DataFrame = pd.read_csv(dataset)

    result = df.groupby('release_year')['id'].aggregate('count')
    result.plot(kind='line', xlabel='Año de lanzamiento', ylabel='Cantidad de películas', title='Películas más populares')
    graph_output(f"{img_path}/movies_by_release_year.png", showing)

    plt.cla()

    result = pd.read_csv('../dataset/movies_by_genre.csv')
    result = result.groupby('genres')['count'].aggregate('sum')
    result.plot(kind='bar', ylabel='Películas', xlabel='Géneros', title='Películas por Género')
    graph_output(f"{img_path}/movies_by_genre.png", showing)

    plt.cla()
    result = df.groupby('original_language')['id'].aggregate('count')
    result.plot(kind='bar', xlabel='Lenguaje Original', ylabel='Cantidad de Películas', title='Películas por lenguaje original')
    graph_output(f"{img_path}/movies_by_original_language.png", showing)

    plt.cla()
    result = df.groupby('release_month')['id'].aggregate('count')
    result.plot(kind='bar', title='Películas por mes de lanzamiento', xlabel='Mes de Lanzamiento', ylabel='Cantidad de Películas')
    graph_output(f"{img_path}/movies_by_release_month.png", showing)

    plt.cla()
    result = df.groupby('release_month')['revenue'].aggregate('mean')
    result.plot(kind='bar', title='Ganancias promedio por mes', xlabel='Mes de lanzamiento', ylabel='Ganancias')
    graph_output(f"{img_path}/revenue_by_release_month.png", showing)

    plt.cla()
    result = df.groupby('release_year')['budget'].aggregate('mean')
    result.plot(kind='line', xlabel='Año de lanzamiento', ylabel='Presupuesto', title='Presupuestos promedio por año')
    graph_output(f"{img_path}/budget_by_year.png", showing)

    plt.cla()
    result = df.groupby('release_year')['revenue'].aggregate('mean')
    result.plot(kind='line', xlabel="Año de lanzamiento", ylabel="Ganancias", title="Ganancias promedio por año")
    graph_output(f"{img_path}/revenue_by_year.png", showing)

    plt.cla()
    result = df.groupby('release_year')['runtime'].aggregate('mean')
    result.plot(kind='line', xlabel='Año de lanzamiento', ylabel='Duración (minutos)', title='Duración promedio por año')
    graph_output(f'{img_path}/runtime_by_year.png', showing)

    plt.cla()
    result = df[['popularity', 'vote_average']]
    result.plot(kind='scatter', x='popularity', y='vote_average', xlabel='Índice de popularidad', ylabel='Calificación promedio', title='Popularidad vs Calificación')
    graph_output(f'{img_path}/vote_average_vs_popularity.png', showing)

    plt.cla()
    result = df[['budget', 'vote_average']]
    result.plot(kind='scatter', x='budget', y='vote_average', xlabel='Presupuesto', ylabel='Calificación promedio', title='Presupuesto vs Calificación')
    graph_output(f'{img_path}/vote_average_vs_budget.png', showing)

    plt.cla()
    df.plot(kind='scatter', x='runtime', y='revenue', title='Duración vs Ganancias', xlabel='Duración (minutos)', ylabel='Ganancias')
    graph_output(f'{img_path}/revenue_vs_runtime.png', showing)