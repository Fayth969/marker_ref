import matplotlib.pyplot as plt
import numpy as np
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
fontdic = {"font": "serif", "size":15, "color": "blue"}
plt.subplot(4, 4, 1)
plt.plot(y1, marker = "o", ls = "dashdot", color = "purple", ms = 12)
plt.plot(y2, marker = "d", ls = "dashed", color = "red",  ms= 12)

plt.title("Fayth Data Visualization", fontdict= fontdic)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(lw= 1.3, color= "k")
x1 = np.array([1, 40])
y1 = np.array([20,250])

plt.subplot(4, 4, 2)
plt.plot(x1, y1, marker = "v", color= "orange", ls = ":")
plt.grid(color = "green", lw= 2.0)
#plt.title("subplot title".upper(), fontdict=fontdic)

plt.subplot(2, 4, 3)
plt.plot(x1, y1, marker = "+", color= "violet", ls = ":")
plt.grid(color = "yellow", lw= 2.0)
#plt.title("subplot title".upper(), fontdict=fontdic)

plt.subplot(2, 4, 4)
plt.plot(x1, y1, marker = "d", color= "red", ls = ":")
plt.grid(color = "violet", lw= 2.0)
#plt.title("subplot title".upper(), fontdict=fontdic)

plt.subplot(2, 4, 5)
plt.plot(x1, y1, marker = "d", color= "red", ls = ":")
plt.grid(color = "violet", lw= 2.0)
#plt.title("subplot title".upper(), fontdict=fontdic)

plt.subplot(2, 4, 6)
plt.plot(x1, y1, marker = "d", color= "red", ls = ":")
plt.grid(color = "violet", lw= 2.0)
#plt.title("subplot title".upper(), fontdict=fontdic)

plt.subplot(2, 4, 7)
plt.plot(x1, y1, marker = "d", color= "red", ls = ":")
plt.grid(color = "violet", lw= 2.0)
#plt.title("subplot title".upper(), fontdict=fontdic)

plt.subplot(2, 4, 8)
plt.plot(x1, y1, marker = "d", color= "red", ls = ":")
plt.grid(color = "violet", lw= 2.0)
#plt.title("subplot title".upper(), fontdict=fontdic)


plt.show()