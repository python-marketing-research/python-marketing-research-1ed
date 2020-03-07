"""
This module contains all function from Chapter 8 of Python for 
Marketing Research and Analytics
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def pca_summary(pca):
  """Return a formatted summary of the PCA fit
  
  arguments:
  pca: a fit PCA() object from sklearn.decomposition
  
  returns:
  a Dataframe containing a summary of the PCA fit statistics
  """
  return pd.DataFrame([pca.explained_variance_,
              pca.explained_variance_ratio_,
              np.cumsum(pca.explained_variance_ratio_)],
             columns=['pc{}'.format(i) for i in
                      range(1, 1+len(pca.explained_variance_))],
             index=['variance',
                    'proportion of variance explained',
                    'cumulative proportion'])


def pca_components(pca, variable_names):
  """Return loading of variables on specific components in the PCA  

  arguments:
  pca: a fit PCA() object from sklearn.decomposition
  variable_names: list of variable names to use as column names

  returns:
  a Dataframe containing the loading of each variable in PCA space
  """
  return pd.DataFrame(pca.components_,
                      index=['pc{}'.format(i+1)
                             for i in range(len(pca.components_))],
                      columns=variable_names).T


def plot_arrow_component(pca_components, variable, scale=1):
  """Plot an arrow of component dimensions in PCA space
  
  arguments:
  pca_components: Output from pca_components()
  variiable: variable name to plot
  """
  plt.arrow(x=0, y=0,
            dx=pca_components.loc[variable]['pc1'] * scale,
            dy=pca_components.loc[variable]['pc2'] * scale,
            color='r',
            head_width=.5, overhang=1)
  plt.text(x=pca_components.loc[variable]['pc1'] * scale,
           y=pca_components.loc[variable]['pc2'] * scale,
           s=variable,
           color='r',
           fontsize=16)


def biplot(values_transformed, pca_components, label=[]):
  """Create a biplot, a scatterplot of points in PCA space with arrows
  representing the loadings of each variable.
  Points can optionally be labelled
  
  arguments:
  values_transformed: PCA-transformed values
  pca_components: Output from pca_components
  label: optional, labels for each data point"""

  scale = 1.2* np.max(values_transformed[:,1])
  plt.figure(figsize=(10, 10))
  for v in pca_components.index:
    plot_arrow_component(pca_components, v, scale)
  plt.scatter(x=values_transformed[:,0],
              y=values_transformed[:,1],
              color='gray')
  if len(label) == values_transformed.shape[0]:
    for i, txt in enumerate(label):
      plt.text(s=txt,
               x=values_transformed[i,0]+.01*scale,
               y=values_transformed[i,1]+.01*scale,
               fontsize=14)
  plt.xlabel('PC1')
  plt.ylabel('PC2')



