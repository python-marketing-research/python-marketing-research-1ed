'''
This module contains all function from Chapter 7 of Python for 
Marketing Research and Analytics
'''
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics import gofplots, regressionplots


def generate_satisfaction_scores(mean, std, size, translation, halo):
  '''Simulate satisfaction scores'''
  sat_scores = np.floor(halo + np.random.normal(loc=mean, scale=std, size=size)
                        + translation)
  sat_scores[sat_scores > 100] = 100
  sat_scores[sat_scores < 0] = 0
  return sat_scores


def plot_gof_figures(model):
  '''Plot a multipanel figure of goodness of fit plots'''
  fig = plt.figure(figsize=(16,16))
  ax = plt.subplot(2,2,1)
  sns.residplot(model.fittedvalues, model.resid, lowess=True)
  plt.xlabel('Fitted values')
  plt.ylabel('Residuals')
  plt.title('Residuals vs Fitted')
  ax = plt.subplot(2,2,2)
  _=gofplots.qqplot(model.resid, fit=True, line='45', ax=ax)
  plt.title('Normal Q-Q')
  ax = plt.subplot(2,2,3)
  plt.scatter(model.fittedvalues, np.abs(model.resid)**.5)
  plt.xlabel('Fitted values')
  plt.ylabel('Square root of the standardized residuals')
  plt.title('Scale-Location')
  ax = plt.subplot(2,2,4)
  _ = regressionplots.plot_leverage_resid2(model, ax=ax)