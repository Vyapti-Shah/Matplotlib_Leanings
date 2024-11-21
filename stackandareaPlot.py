import matplotlib.pyplot as plt

x = [1,2,3,4,5]
area = [2,3,2,5,4]
area1 = [2,3,4,5,6]
area2 = [1,3,2,4,2]
l = ["area","area1","area2"]
plt.stackplot(x,area,area1,area2,labels=l,colors=["r","g","b"],baseline="sym") #baseline can be zero,wiggle,sym
plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(loc=2)
plt.show()