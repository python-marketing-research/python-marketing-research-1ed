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
  """Returns the mean values for each dimension in the data, broken down by the
  factor specified in labels
  
  arguments:
  data: DataFrame with data of interest
  labels: Series or array with length matching the row count of data. data will
    be broken down by the values in labels
  
  returns:
  DataFrame with labels in rows and mean value for each label value for every
    column in data in the columns
  """
  print(list(zip(*np.unique(labels, return_counts=True))))
  
  return pd.pivot_table(data,
                        index=labels)


def cluster_plot_raw(x, y, labels):
  """Generates a scatter plot of the points in x and y color coded based on
    values in labels
  
  arguments:
  x: values to be plotted along x-axis
  y: values to be plotted along y-axis
  labels: group identity for each point, which will be indicated by color
  """
  for l in np.unique(labels):
    idx = labels == l
    plt.scatter(x[idx],
                y[idx],
                label=l)
  plt.legend()
  plt.xlabel(x.name)
  plt.ylabel(y.name)


def cluster_plot(data_df, labels):
  """Generates a scatter plot of the points in the first two PCA dimensions of
    data_df, color coded based on values in labels
  
  arguments:
  data_df: DataFrame containing the data of interest
  labels: Series or array with length matching the row count of data_df that
    specifies the group identity of each row, which will be indicated by color
    in the scatter plot
  """
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
  plt.xlabel('First principal component')
  plt.ylabel('Second principal component')