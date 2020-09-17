#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:17:55 2020

@author: nikhildhamne
"""
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-1,1,50), np.linspace(-1,1,50))
d = np.sqrt(x*x+y*y)
sigma, mu = 0.25, 0.0
g = np.round(np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) ),2)
print("2D Gaussian-like array:")
print(g)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot a 3D surface
ax.plot_surface(x, y, g)

plt.show()
