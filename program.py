import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import datetime as dt
from sklearn.cluster import DBSCAN
def get_infected_names(input_name, df):
    epsilon = 0.0018288  # A radial distance of 6 feet in kilometers
    min_samples = 3
    metric = 'haversine'
    model = DBSCAN(eps=epsilon, min_samples=min_samples, metric=metric).fit(np.radians(coordinates_df))
    df['cluster'] = model.labels_
    input_name_cluster = df.loc[df['id'] == input_name, 'cluster'].values[0]
    if input_name_cluster == -1:
        return [] 
    infected_names = df[df['cluster'] == input_name_cluster]['id'].tolist()
    infected_names = [name for name in infected_names if name != input_name]
    distinct_infected_names = list(set(infected_names))
    return distinct_infected_names
infected_names = get_infected_names('Alice', df)
print(infected_names)
