"""
This module contains all function from Chapter 7 of Python for 
Marketing Research and Analytics
"""

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics import gofplots, regressionplots


def generate_satisfaction_scores(mean, std, halo,
                                 score_range=(0, 100)):
  """Simulate satisfaction scores of a survey questions from normal
  distributions.
  
  arguments:
  mean: desired mean of satisfaction score distribution
  std: desired standard deviation of satisfaction score distribution
  halo: an array of individual-level effects, sets the size of returned array
  score_range: tuple of form (max, min), values outside range are clipped

  returns:
  scores: array of simulated satisfaction scores
"""

  # Draw scores from a normal distribution
  scores = np.random.normal(loc=mean, scale=std, size=len(halo))
  
  # Add the halo
  scores = scores + halo
  
  # Floor the scores so that they are all integers and clip to limit range
  scores = np.floor(scores)
  scores = np.clip(scores, score_range[0], score_range[1])

  return scores


def plot_gof_figures(model):
  """Plot a multipanel figure of goodness of fit plots
  
  arguments:
  model: a fitted ols() object from statsmodels.formula.api
  
  output:
  Prints a multipanel figure including:
  * Residual vs fitted value plot
  * Scale-location plot
  * Q-Q plot
  * Leverage vs normalized residual plot
  """
  
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