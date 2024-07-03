import pandas as pd
import pingouin as pg

def stat_test(dataset: str): 
    df = pd.read_csv(dataset)
    anova = pg.anova(data=df, dv='revenue', between='release_year', detailed=True)
    print(anova)