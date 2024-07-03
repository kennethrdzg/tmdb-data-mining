import pandas as pd
import pingouin as pg

def stat_test(df: pd.DataFrame): 
    anova = pg.anova(data=df, dv='revenue', between='release_year', detailed=True)
    print(anova)