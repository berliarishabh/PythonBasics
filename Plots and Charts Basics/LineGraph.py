#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : LineGraph.py
#date : 2016.10.31
#purpose : Line Graph plot of random data [10,100]
#version: 1.0.0


import random
import matplotlib.pyplot as plt
import numpy as np


minNumber = 10
maxNumber = 100

x = random.sample(range(10,100),25)

plt.plot(x, color='black')
plt.xlabel("Numbers")
plt.ylabel("Values")
groups=len(yaxis)
index = np.arange(groups)
barWidth = 0.8
plt.title("Line Graph of Random Numbers (10-100)")
plt.xticks(index + barWidth, xaxis, rotation='vertical' )

plt.show()
