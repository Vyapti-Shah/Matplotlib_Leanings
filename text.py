import matplotlib.pyplot as plt

x = [1,2,3,4,6]
y = [3,1,4,2,6]

plt.plot(x,y)
plt.title("Data",fontsize=15)
plt.xlabel("days",fontsize=15)
plt.ylabel("languages",fontsize=15)
plt.text(5,5,"python",fontsize=12,style="italic",bbox={"facecolor":"y"})
plt.annotate("java",style="italic",xy=(3,4),xytext=(4,4),bbox={"facecolor":"y"},arrowprops=dict(facecolor="black",shrink=100))
plt.legend(["up"],loc=9,facecolor="g",edgecolor="r",framealpha=0.3,shadow=True)
plt.show()
