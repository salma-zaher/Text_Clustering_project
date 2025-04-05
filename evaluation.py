# -*- coding: utf-8 -*-
"""evaluation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CJHiwiRJ6DYLh1mAwDsaTFEz4E0J1WnR
"""

from sklearn.metrics import silhouette_score
import numpy as np
from collections import Counter

def purity_score(y_true, y_pred):
    contingency_matrix = np.zeros((np.max(y_pred) + 1, np.max(y_true) + 1))

    for i in range(len(y_true)):
        contingency_matrix[y_pred[i], y_true[i]] += 1

    return np.sum(np.max(contingency_matrix, axis=1)) / np.sum(contingency_matrix)

def evaluate_clustering(labels, features):

    return silhouette_score(features, labels)