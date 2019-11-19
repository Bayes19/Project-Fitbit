import pandas as pd
import numpy as np
from prep import prep_df, test_train_split
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = prep_df()
df.isnull().sum()
X = df.Date
y = df.Steps

X = np.array(X)
y = np.array(y)

from sklearn.model_selection import TimeSeriesSplit
tss = TimeSeriesSplit(n_splits=4, max_train_size=None)

for train_index, test_index in tss.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]


#all graphs
groups = [0, 1, 2, 3, 5, 6, 7, 8, 9]
i = 1
plt.figure(figsize=(25,7))
values = df.values
for group in groups:
	plt.subplot(len(groups), 1, i)
	plt.plot(values[:, group])
	plt.title(df.columns[group], y=0.5, loc='right')
	i += 1
plt.show()
