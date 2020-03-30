"""
This module contains all function from Chapter 6 of Python for 
Marketing Research and Analytics
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def ttest(a, b):
  """This function displays statistics on two groups, runs a t-test, and finds
  the 95% confidence interval of the mean difference between groups
  
  arguments:
  a, b: numpy arrays of numeric type
  
  Prints the following:
  * Mean and standard deviation of a and b
  * Welch's t-test statistic testing the equality of means of a and b
  * 95% confidence interval of the mean difference between a and b"""
  
  # Get means and standard deviation of each group
  mean_a = a.mean() 
  mean_b = b.mean()
  
  std_a = a.std()
  std_b = b.std()
  
  print('Group a - mean: {0}  standard deviation: {1}'.format(mean_a, std_a))
  print('Group b - mean: {0}  standard deviation: {1}\n'.format(mean_b, std_b))
  
  # Run a Welch's t-test between the groups
  ttest_out = stats.ttest_ind(a, b, equal_var=False)
  print("Welch's t-test statistic: {0}\np-value: {1}\n"
        .format(ttest_out.statistic, ttest_out.pvalue))
  
  # Find the 95% confidence interval using scipy.statst.interval function
  # The difference in means is the location of the distribution (loc parameter)
  # The geometric mean of the standard error of each group is the scale
  count_a = a.shape[0]
  count_b = b.shape[0]
  dof = count_a + count_b - 2
  
  geometric_mean_sem = np.sqrt(((count_a - 1) * stats.sem(a)**2
                                + (count_b -1) * stats.sem(b)**2)/dof)
  print('95% confidence interval of the mean difference between a and b: {0}'
        .format(stats.t.interval(alpha=0.95, df=dof,
                                 loc=mean_a - mean_b,
                                 scale=geometric_mean_sem)))


def plot_confidence_intervals(centers, conf_ints, zero_line=False):
  """Plot centers and confidence intervals
  
  arguments:
  centers: Series containing center poitns (mean values)
  conf_ints: Dataframe containing the lower bound in the 0th column and upper
             bound in the 1st
  zero_line: Boolean specifying whether to include a line at x=0 (optional,
             default False)"""
  
  plt.figure(figsize=(8,4))
  sort_index = np.argsort(centers.values)
  centers = centers[sort_index]
  conf_ints = conf_ints.iloc[sort_index]
  plt.barh(y=range(len(centers)), left=conf_ints[0],
           width=conf_ints[1]-conf_ints[0],
           height=0.2, color='0.4')
  plt.yticks(range(len(centers)), conf_ints.index)
  plt.plot(centers, range(len(centers)), 'ro')
  if zero_line:
    plt.plot([0,0],[-.5, len(centers) - 0.5], 'gray',
             linestyle='dashed')
    plt.xlim((-.05, 1.1 * conf_ints.iloc[:,1].max()))
  plt.ylim((-.5, len(centers) - 0.5))

