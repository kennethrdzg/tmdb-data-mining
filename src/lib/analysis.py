import pandas as pd

def print_buffer(): 
    print("-"*20)

def analyze(dataset: str): 
    df: pd.DataFrame = pd.read_csv(dataset)

    result = df['genres'].aggregate('count')

    # print("Combinaciones distintas de géneros: ", result)
    # print_buffer()
    
    result = df.groupby('original_language')['id'].aggregate('count')
    print("Películas por idioma original:", result)
    print_buffer()

    # result = df.groupby('production_companies')['id'].aggregate('count')
    # print("Compañías productoras: ", result)
    # print_buffer()

    result = df['release_date'].aggregate(['min', 'max'])
    print("Fecha de estreno más antigua:", result['min'])
    print("Fecha de estreno más reciente:", result['max'])
    print_buffer()

    result = df['popularity'].aggregate(['average', 'min', 'max'])
    print("Popularidad más baja:", result['min'])
    print("Popularidad más baja:", result['max'])
    print("Popularidad promedio:", round(result['average'], 2))
    print_buffer()

    result = df['vote_average'].aggregate(['average', 'min', 'max'])
    print("Peor calificación:", result['min'])
    print("Mejor calificación:", result['max'])
    print("Calificación promedio:", round(result['average'], 2))
    print_buffer()

    result = df['budget'].aggregate(['average', 'max'])
    print("Presupuesto promedio:", round(result['average'], 2))
    print("Presupuesto más grande:", result['max'])
    print_buffer()

    result = df['revenue'].aggregate(['average', 'min', 'max'])
    print("Ganancias promedio:", round(result['average'], 2))
    print("Menor ganancias:", result['min'])
    print("Mayor ganancias:", result['max'])
    print_buffer()

    result = df.groupby('release_year')['id'].aggregate('count')
    print("Cantidad de películas por año:")
    print(result)
    print_buffer()

    genres: dict = dict()
    result = df.groupby('genres')['id'].aggregate('count')
    for indx, value in result.items(): 
        values = str(indx).lstrip('[')
        values = values.rstrip(']')
        values = values.split(', ')
        for val in values: 
            val = val.strip('\'')
            if val not in genres: 
                genres[val] = 1
            else: 
                genres[val] += 1
    genre_list = list()
    genre_count = list()
    for genre, num in genres.items(): 
        genre_list.append(genre)
        genre_count.append(num)
    new_df = {
        "genres": genre_list, 
        "count": genre_count
    }
    new_df = pd.DataFrame(new_df)
    new_df = new_df.groupby('genres')['count'].aggregate('sum')
    new_df.to_csv(f'../dataset/movies_by_genre.csv')