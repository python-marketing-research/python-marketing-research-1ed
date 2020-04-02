"""
This module contains all function from Chapter 8 of Python for 
Marketing Research and Analytics
"""

import numpy as np
import scipy.stats as ss
import sklearn.preprocessing as pp
from statsmodels.stats.outliers_influence import variance_inflation_factor


def autotransform(x):
  """Return scaled Box-Cox transform of x
  
  arguments:
  x: numpy array of numerics
  
  returns:
  Box-Cox transformed and scaled copy of x
  """
  x_bc, lmbd = ss.boxcox(1 + x)
  return pp.scale(x_bc)

def print_variance_inflation_factors(model):
  """Print the variance inflation factor for each parameter in a model
  
  arguments:
  model: a fit statsmodels ols object
  """
  for i, param in enumerate(model.params.index):
    print('VIF: {:.3f}, Parameter: {}'.format(
        variance_inflation_factor(model.model.exog, i), param))