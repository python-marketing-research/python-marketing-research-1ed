'''
This module contains all function from Chapter 3 of Python for 
Marketing Research and Analytics
'''


def iqr(x):
  '''Return the interquartile range of the input numpy array'''
  return x.quantile(0.75) - x.quantile(0.25)

