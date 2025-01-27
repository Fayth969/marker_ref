import matplotlib. pyplot as plt
import numpy as np

grade=np.array(['A','B','C','D','E'])
student=np.array([400,600,700,30,28])
colors=('black','blue','yellow','grey','red')
fontdict={'font':'arial','size':15,'color':'red'}
color={'color':'blue'}
plt.title('STUDENT BAR CHART'.upper(),color= 'r')
plt.bar(grade, student, color=colors)
plt.xlabel("student grades", fontdict=color)
plt.ylabel("total student scores",fontdict=color)
plt.show()