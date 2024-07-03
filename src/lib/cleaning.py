import pandas as pd

def clean_data(input_filename: str, output_filename: str)->pd.DataFrame: 
    df = pd.read_csv(input_filename)

    print("Limpiando datos...")

    df = df.dropna()
    df = df.drop_duplicates()
    release_year = []
    release_month = []
    for x in df.index: 
        if df.loc[x, 'budget'] <= 0 or df.loc[x, 'revenue'] <= 0: 
            df.drop(x, inplace=True)
            continue
        release_date: list = df.loc[x, 'release_date'].split("-")
        release_year.append(release_date[0])
        release_month.append(release_date[1])
    
    df['release_year'] = release_year
    df['release_month'] = release_month
    
    df.to_csv(output_filename)
    print("Limpieza concluida.")
