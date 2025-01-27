import matplotlib.pyplot as plt
import numpy as np
#first plot
xaxis = np.array([10, 40, 80, 1])
yaxis = np.array([500, 15, 25, 44])
x = np.array([10, 25])
y = np.array([2, 210])
plt.subplot(2, 3, 1)
plt.plot(xaxis, yaxis, x, y, marker = 'o', ls = 'dashdot', ms=5, mec='r', mfc='yellow') #fmt standard
fontdic = {
    'font' : 'arial',
    'size' : 15,
    'color' : 'red'
}
color = {
    'color' : 'blue'
}
plt.title('real time analysis'.upper(), fontdict=fontdic, loc='center')
# plt.xlabel('x data'.upper(), fontdict=color)
# plt.ylabel('y data'.upper(), fontdict=color)
plt.grid(color='k', linewidth=2)
#second plot
xvalue = np.array([20, 250])
yvalue = np.array([10, 150])
plt.subplot(2, 3, 2)
plt.grid(lw=1.3)
plt.title('second plot'.upper(), fontdict=color)
plt.plot(xvalue, yvalue, ls=':', c='r')


#third plot is a bar chart
grades = np.array(['A', 'B', 'C', 'D', 'F'])
Students = np.array([100, 150, 45, 60, 32])
colors = ['green', 'blue', 'yellow', 'grey', 'red']
c = {
    'color' : 'red'
}
plt.subplot(2, 3, 3)
plt.title('Bar Chart', fontdict=c)
plt.bar(grades, Students, color=colors)
plt.xlabel('students grades', fontdict=c)
plt.ylabel('total student scores', fontdict=c)
plt.grid()

#fourth plot is a pie chart
grades_percentage = np.array([25.8, 38.8, 11.6, 15.5, 8.3])
label = ['A', 'B', 'C', 'D', 'F']
plt.subplot(2, 3, 4)
plt.title('pie chart', fontdict=c)
plt.pie(grades_percentage, labels=label, autopct='%1.1f%%', colors=colors)
plt.legend(label, title='grades', loc='best')
plt.suptitle('Data VISUALIZATION'.upper(), c='r')
plt.show()


"""
marker = blue by default use o
linestyle = blue by default use red
make the linestyle dashed dot the symbol is -.  
"""