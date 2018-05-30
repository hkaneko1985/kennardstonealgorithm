# -*- coding: utf-8 -*- %reset -f
"""
@author: Hiromasa Kaneko
Demonstration of Kennard-Stone algorighm
"""

import matplotlib.pyplot as plt
import numpy as np

import kennardstonealgorithm

number_of_samples = 50
number_of_selected_samples = 20

# generate samples 0f samples for demonstration
X = np.random.rand(number_of_samples, 2)

# standarize X
autoscaled_X = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)

# select samples using Kennard-Stone algorithm
selected_sample_numbers, remaining_sample_numbers = kennardstonealgorithm.kennardstonealgorithm(
    autoscaled_X, number_of_selected_samples)
print("selected sample numbers")
print(selected_sample_numbers)
print("---")
print("remaining sample numbers")
print(remaining_sample_numbers)

# plot samples
plt.figure()
plt.scatter(autoscaled_X[:, 0], autoscaled_X[:, 1], label="all samples")
plt.scatter(autoscaled_X[selected_sample_numbers, 0], autoscaled_X[selected_sample_numbers, 1], marker="*",
            label="all samples")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend(loc='upper right')
plt.show()
