import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.plot(x,y,color="r") #linear plot
plt.fill_between(x,y)
plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

a = [1,2,3,4,5]
b = [1,2,3,4,5]
plt.plot(a,b,color="g") #linear plot
plt.fill_between(x=[2,4],y1=2,y2=4)
plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

c = np.array([1,2,3,4,5])
d = np.array([1,2,3,4,5])
plt.plot(c,d,color="g") #linear plot
plt.fill_between(c,d,where=(c >= 2)&(c <= 4),alpha=0.5) #for using <= and >= we need numpy 
plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()