import pandas as pd
import numbers
import matplotlib.pyplot as plt
import statsmodels.api as sm
from io import StringIO
from os import path, mkdir

def transform_variable(df: pd.DataFrame, x: str) -> pd.Series: 
    if isinstance(df[x][0], numbers.Number): 
        print("Hi")
        return df[x]
    else: 
        return pd.Series([i for i in range(len(df[x]))])

def linear_regression(df: pd.DataFrame, x: str, y: str) -> dict[str, float]: 
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()

    html_string = model.summary().tables[1].as_html()
    summary_buffer = StringIO(html_string)

    #bands = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col= 0)[0]
    bands = pd.read_html(summary_buffer, header=0, index_col=0)[0]
    print("Bands")
    print(bands)
    print(bands.iloc[0, 4])
    print("BYE")
    html_string = model.summary().tables[1].as_html()
    summary_buffer = StringIO(html_string)
    coef = pd.read_html(summary_buffer,header=0,index_col=0)[0]['coef']

    html_string = model.summary().tables[0].as_html()
    summary_buffer = StringIO(html_string)
    r_2_t = pd.read_html(summary_buffer,header=None,index_col=None)[0]

    #return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands['[0.025'][0], 'hi_band': bands['0.975]'][0]}
    return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands.iloc[0, 4], 'hi_band': bands.iloc[0, 5]}


def plt_lr(df: pd.DataFrame, x: str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: tuple[str, str]): 
    fixed_x = transform_variable(df=df, x=x)
    df.plot(x=x, y=y, kind='scatter')
    plt.plot(df[x], [m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x], [m * x + low_band for _, x in fixed_x.items()], [m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])

def forecast(dataset: str, showing = False): 
    df = pd.read_csv(dataset)
    df['release_date'] = pd.to_datetime(df['release_date'])

    df_by_revenue = df.groupby('release_date')['revenue'].mean().reset_index()

    a = linear_regression(df_by_revenue, x='release_date', y='revenue')
    print(a)
    plt_lr(df=df_by_revenue, x='release_date', y='revenue', colors=('red', 'orange'), **a)
    if showing: 
        plt.show()
    else: 
        if not path.exists('img'): 
            mkdir('img')
        if not path.exists('img/forecast'): 
            mkdir('img/forecast')
        plt.savefig('img/forecast/forecast.png')
    return
 