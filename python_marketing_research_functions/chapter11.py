"""
This module contains all function from Chapter 11 of Python for 
Marketing Research and Analytics
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import clone, decomposition


def return_precision_recall(y_true, y_pred, model):
  """Return the precision and recall performance of the model
  
  arguments:
  y_true: ground truth label values
  y_pred: predicted label values
  model:  a fit sklearn classifier, e.g. GaussianNB, RandomForestClassifier, etc
  
  returns:
  A dataframe with precision, recall, and f1-score (in rows)
    for each class (in columns)
  """
  conf_mat = metrics.confusion_matrix(y_true, y_pred)

  precision = pd.Series(metrics.precision_score(y_test,
                                                y_pred,
                                                average=None),
                        index=model.classes_)
  recall = pd.Series(metrics.recall_score(y_test,
                                          y_pred,
                                          average=None),
                     index=model.classes_)
  
  f1 = pd.Series(2 * (precision * recall)/(precision + recall),
                 index=model)

  return pd.DataFrame([precision, recall, f1], index=['precision',
                                                      'recall', 'f1'])


def plot_decision_pca(model, X, y):
  """Creates a figure representing the model decision boundaries in PCA space
  
  arguments:
  model: a fit sklearn classifier, e.g. GaussianNB, RandomForestClassifier, etc
  X: test input data
  y: test ground truth labels
  """
  width, height = 500, 500

  # Transform the X values using a PCA
  p = decomposition.PCA(random_state=132, svd_solver='full')
  X_transformed = p.fit_transform(X.iloc[:,:2])

  # Pull the first two dimensions
  x0 = X_transformed[:, 0]
  x1 = X_transformed[:, 1]

  # Get evenly spaced values between the min and max values
  x0_g = np.linspace(x0.min(), x0.max(), width)
  x1_g = np.linspace(x1.min(), x1.max(), height)

  # Create a "grid" of those evenly spaced values from each vector
  xx, yy = np.meshgrid(x0_g, x1_g)

  # Stack together all of the sampled values 
  X_grid_transformed = np.vstack([xx.ravel(), yy.ravel()]).T

  # Do the inverse transform to get the non-PCA transformed values
  X_grid = p.inverse_transform(X_grid_transformed)

  # Fit a clone of the model using use inverse transformed columns
  # From the first two PCA dimensions.
  # Predict values on the sampled values
  model_c = clone(model)
  model_c.fit(p.inverse_transform(np.vstack([x0, x1]).T), y)
  X_grid_labels = model_c.predict(X_grid)

  # Create a class mapper to map from class string to an integer
  class_mapper = {c:i for i,c in enumerate(model.classes_)}

  plt.figure(figsize=(6,6))
  # Plot the predicted values
  a = plt.scatter(X_transformed[:, 0], X_transformed[:, 1],
                  c=[class_mapper[l] for l in y],
                  cmap=plt.cm.rainbow, edgecolor='k', vmin=0, vmax=3)
  plt.contourf(xx, yy,
               np.reshape([class_mapper[l] for l in X_grid_labels],
                          (width, height)),
              cmap=a.cmap, alpha=0.5, levels=3)
  cb = plt.colorbar(ticks=[0.5, 1.2, 2, 2.8])
  _ = cb.ax.set_yticklabels(model.classes_)
  plt.title('Decision boundaries with true values overlaid')
  plt.xlabel('First principle component')
  plt.ylabel('Second principle component')


def pairwise_decision_boundary(model, X_train, y_train,
                               X_test, y_test,
                               first_column, second_column,
                               jitter=False):
  """Creates a figure representing the model decision boundaries in any two 
  columns within the input data
  
  arguments:
  model: a fit sklearn classifier, e.g. GaussianNB, RandomForestClassifier, etc
  X_train: training input data
  y_train: ground truth labels for training data
  X_test: test (holdout) input data
  y_test: ground truth labels for test (holdout) data
  first_column: input data column name to display on x-axis
  second_column: input data columns name to display on y-axis
  jitter: if True, data points will be jittered (i.e. if input data are categorical)
  """
  width, height = 1000, 1000
  # Create a class mapper to map from class string to an integer
  class_mapper = {c:i for i,c in enumerate(model.classes_)}
  
  x0 = X_train[first_column]
  x1 = X_train[second_column]
  # Get evenly spaced values between the min and max values
  x0_g = np.linspace(x0.min(), x0.max(), width)
  x1_g = np.linspace(x1.min(), x1.max(), height)
  
  # Create a "grid" of those evenly spaced values from each vector
  xx, yy = np.meshgrid(x0_g, x1_g)   
  # Stack together all of the sampled values
  X_grid = np.vstack([xx.ravel(), yy.ravel()]).T    
  
  model_c = clone(model)
  model_c.fit(X_train.loc[:,[first_column, second_column]], y_train)
  X_grid_labels = model_c.predict(X_grid)
  # Plot the predicted values
  j_x0, j_x1 = 0, 0
  if jitter:
    j_x0 = (np.random.random(X_test.shape[0])-0.5)/10.
    j_x1 = (np.random.random(X_test.shape[0])-0.5)/10.
  a = plt.scatter(X_test[first_column] + j_x0,
                  X_test[second_column] + j_x1,
                  c=[class_mapper[l] for l in y_test],
                  cmap=plt.cm.rainbow, 
                  edgecolor='k', vmin=0, vmax=3)
  plt.contourf(xx, yy,
               np.reshape([class_mapper[l] for l in X_grid_labels],
                          (width, height)),
              cmap=a.cmap, alpha=0.5, levels=3)
  plt.title('Decision boundaries with true values overlaid')
  plt.xlabel(first_column)
  plt.ylabel(second_column)
  cb = plt.colorbar(ticks=[0.5, 1.2, 2, 2.8])
  cb.ax.set_yticklabels(model.classes_)