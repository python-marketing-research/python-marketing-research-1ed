'''
This module contains all function from Chapter 8 of Python for 
Marketing Research and Analytics
'''
import numpy as np
import scipy.stats as ss
import sklearn.preprocessing as pp


def autotransform(x):
  '''Return scaled Box-Cox transform of x'''
  x_bc, lmbd = ss.boxcox(1 + x)
  return pp.scale(x_bc)

