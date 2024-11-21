import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.step(x,y,marker="o")
plt.grid()
plt.show()

a = [1,2,3,4,5]
b = [1,3,2,5,4]
plt.step(a,b,color="g",label="python",marker="o",ms=10,mfc="b") #ms=marker size and mfc=marker face color
plt.grid()
plt.legend(loc=2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()