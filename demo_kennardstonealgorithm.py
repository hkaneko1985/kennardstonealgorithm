# -*- coding: utf-8 -*- %reset -f
"""
@author: Hiromasa Kaneko
Demonstration of Kennard-Stone algorighm
"""

import numpy as np
import matplotlib.pyplot as plt
import kennardstonealgorithm

numberofsamples = 50
numberofselectedsamples = 20

# generate samples 0f samples for demonstration
X = np.random.rand(numberofsamples,2)

# standarize X
autoscaledX = (X - X.mean()) / X.std(ddof=1)

# select samples using Kennard-Stone algorithm
selectedsamplenumbers, remainingsamplenumbers = kennardstonealgorithm.kennardstonealgorithm( autoscaledX, numberofselectedsamples )
print( "selected sample numbers")
print( selectedsamplenumbers )
print( "---" )
print( "remaining sample numbers" )
print( remainingsamplenumbers )

# plot samples
plt.figure()
plt.scatter( autoscaledX[:,0], autoscaledX[:,1], label = "all samples")
plt.scatter( autoscaledX[selectedsamplenumbers,0], autoscaledX[selectedsamplenumbers,1], marker="*", label = "all samples")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend(loc='upper right')
plt.show()
