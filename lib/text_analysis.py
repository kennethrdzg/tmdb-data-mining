from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from os import path, mkdir

def create_wordcloud(df: pd.DataFrame, column: str, showing: bool): 
    if not path.exists('img'): 
        mkdir('img')
    if not path.exists('img/wordclouds'): 
        mkdir('img/wordclouds')
    
    words = ""
    for x in df.index: 
        title: str = df.loc[x, column]
        title = title.upper()
        temp_words = title.strip().split(" ")
        words += " ".join(temp_words) + " "
    word_list = words.strip().split(" ")

    all_words = ""
    for w in word_list: 
        all_words += w + " "

    cloud = WordCloud(background_color='white', min_font_size=5).generate(all_words)
    plt.close()
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.imshow(cloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.title(f'{column.upper()} WORD CLOUD')
    
    if showing: 
        plt.show()
    else: 
        plt.savefig(f'img/wordclouds/{column}_wordcloud.png')

def analyze_text(df: pd.DataFrame, showing = False): 
    create_wordcloud(df, 'title', showing)
    create_wordcloud(df, 'overview', showing)
    create_wordcloud(df, 'tagline', showing)