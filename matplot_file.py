import matplotlib.pyplot as plt
import numpy as np

xaxis = np.array([10, 40, 80, 1])
yaxis = np.array([500, 15, 25, 44])
plt.plot(xaxis, yaxis, marker = 'o', ls = 'dashdot', color = 'red') #fmt standard
plt.show()


"""
marker = blue by default use o
linestyle = blue by default use red
make the linestyle dashed dot the symbol is -.  
"""