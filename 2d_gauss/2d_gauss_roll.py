#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:25:04 2020

@author: nikhildhamne
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:17:55 2020

@author: nikhildhamne
"""
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

n=10
weight_matrix = []

x, y = np.meshgrid(np.linspace(-1,1,n), np.linspace(-1,1,n))
d = np.sqrt(x*x+y*y)
sigma, mu = 0.25, 0.0
g = np.round(np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) ),2)
g = np.roll(g,(n//2)+1,axis=0)
g = np.roll(g,(n//2)+1,axis=1)
print("2D Gaussian-like array:")
print(g)

g1=g
#file1 = open("myfile.txt","w") 

for i in range(n):
    for j in range(n):
        g1 = np.roll(g1,1,axis=1)
        #print(g1)
        '''with open('your_file.txt', 'w') as f:
            for item in g1:
                f.write("%s\n" % item)'''
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, g1)
        plt.show()
        #plt.savefig('plot {0}{1}.jpg'.format(i,j))
    g1 = np.roll(g1,1,axis=0)

