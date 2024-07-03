import pandas as pd
import matplotlib.pyplot as plt
from random import randint
from math import inf, sqrt
from os import path, mkdir

def get_points(df: pd.DataFrame, column_x: str, column_y: str)->tuple[list, list]: 
    x_values = list()
    y_values = list()

    for x in df.index: 
        if x == 0: 
            continue
        x_values.append(df.loc[x, column_x])
        y_values.append(df.loc[x, column_y])
    return (x_values, y_values)

def get_centroids(k: int, x_values: list, y_values: list)->list: 
    centroids = list()
    size = len(x_values)
    for _ in range(k): 
        idx = randint(0, size - 1)
        c = (x_values[idx], y_values[idx])
        while c in centroids: 
            idx = randint(0, size - 1)
            c = (x_values[idx], y_values[idx])
        centroids.append(c)
    return centroids

def get_distance(centroid: tuple, point: tuple): 
    x = centroid[0] - point[0]
    y = centroid[1] - point[1]
    return sqrt( (x ** 2 + y **2) )

def get_new_centroid(cluster: list)->tuple: 
    x_sum = 0
    y_sum = 0
    for x, y in cluster: 
        x_sum += x
        y_sum += y
    return (x_sum/len(cluster), y_sum/len(cluster))

def cluster_data(df: pd.DataFrame, columnx_x: str, column_y: str, showing: bool, k = 3): 
    if not path.exists('img'): 
        mkdir('img')
    if not path.exists('img/clusters'): 
        mkdir('img/clusters')

    x_values, y_values = get_points(df, column_x=columnx_x, column_y=column_y)
    centroids = get_centroids(k, x_values, y_values)

    new_clusters = list()
    old_clusters = None

    while old_clusters != new_clusters: 
        del old_clusters
        
        old_clusters = new_clusters
        new_clusters = [ [] for _ in centroids]

        for idx in range(len(x_values)): 
            distance = 0
            smallest_distance = inf
            smallest_idx = -1

            for c in range(len(centroids)): 
                distance = get_distance(centroids[c], (x_values[idx], y_values[idx]))
                if distance < smallest_distance: 
                    smallest_distance = distance
                    smallest_idx = c
                new_clusters[smallest_idx].append((x_values[idx], y_values[idx]))
        centroids = []
        for i in range(k): 
            centroids.append(get_new_centroid(new_clusters[i]))
    plt.cla()
    for cluster in new_clusters: 
        x_values = []
        y_values = []

        for x, y in cluster: 
            x_values.append(x)
            y_values.append(y)
        plt.scatter(x=x_values, y=y_values)
    plt.title(f'{columnx_x.upper()} vs. {column_y.upper()}')
    plt.xlabel(f'{columnx_x.upper()}')
    plt.ylabel(f'{column_y.upper()}')
    if showing: 
        plt.show()
    else: 
        plt.savefig(f'img/clusters/{columnx_x}_vs_{column_y}_cluster.png')

def cluster(df: pd.DataFrame, showing = False):
    cluster_data(df, 'budget', 'revenue', showing=showing)
    cluster_data(df, 'runtime', 'revenue', showing=showing)
    cluster_data(df, 'budget', 'popularity', showing=showing)
    cluster_data(df, 'budget', 'vote_average', showing=showing)
    cluster_data(df, 'vote_average', 'popularity', showing=showing)