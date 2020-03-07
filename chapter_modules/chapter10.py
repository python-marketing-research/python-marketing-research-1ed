"""
This module contains all function from Chapter 10 of Python for 
Marketing Research and Analytics
"""

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
from sklearn import decomposition, preprocessing

def check_clusters(data, labels):
  print(list(zip(*np.unique(labels, return_counts=True))))
  
  return pd.pivot_table(data,
                        index=labels)


def cluster_plot_raw(x, y, labels):
  for l in np.unique(labels):
    idx = labels == l
    plt.scatter(x[idx],
                y[idx],
                label=l)
  plt.legend()
  plt.xlabel(x.name)
  plt.ylabel(y.name)


def cluster_plot(data_df, labels):
  p = decomposition.PCA(random_state=132, svd_solver='full')
  scaled_transformed = p.fit_transform(preprocessing.scale(data_df))
  for l in np.unique(labels):
    idx = np.where(labels == l)[0]
    plt.scatter(scaled_transformed[idx, 0],
                scaled_transformed[idx, 1],
                label=l)
  plt.legend()
  plt.title('First two components explain {}% of the variance'
            .format(round(100*p.explained_variance_ratio_[:2].sum())))
  plt.xlabel('First principle component')
  plt.ylabel('Second principle component')