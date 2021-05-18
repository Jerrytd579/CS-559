from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from dask import dataframe as dd

test = pd.read_csv('mnist_test.csv')
#dask_df = dd.read_csv('huge_data.csv')
train = pd.read_csv('mnist_train.csv')