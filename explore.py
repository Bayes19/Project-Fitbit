import pandas as pd
import numpy as np
from prep import prep_df, test_train_split
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = prep_df()
df.isnull().sum()


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


