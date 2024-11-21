import matplotlib.pyplot as plt

day = [1,2,3,4,5,6,7]
no = [2,3,4,1,5,6,2]
colors = [10,20,30,40,50,60,70]
sizes = [400,200,500,300,600,100,200]
plt.scatter(day,no,c=colors,cmap="viridis",s=sizes,alpha=0.6,marker="*",edgecolor="b") #alpha always between 0 to 1
t = plt.colorbar()
t.set_label("Color Bar",fontsize=10)
plt.title("Scatter Plot",fontsize=10)
plt.xlabel("Day",fontsize=10)
plt.ylabel("No.",fontsize=10)
plt.show()