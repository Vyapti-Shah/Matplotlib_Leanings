import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
ex = [0.4,0.0,0.0,0.0]

plt.pie(x,labels=y,
        explode=ex, #to take the part outside (as here c comes thoda bahar)
        autopct="%0.1f%%",shadow=True,radius=1.5,labeldistance=0.8,startangle=180,textprops={"fontsize":15},
        counterclock=False,wedgeprops={"linewidth":5,"edgecolor":"y"},center=(3,6))
plt.title("data")
plt.legend(loc=1) #loc=1 places the label in 1st quadrant
plt.show()

#Circle Pie Chart
plt.pie([1]) #radius=1
plt.show()

#Double Pie Chart
c = ["r","b","g","y"]
y = ["c","c++","java","python"]
x1 = [40,30,20,10]
plt.pie(x,labels=y,radius=1.5)
plt.pie(x,radius=1,colors=c)
plt.legend()
plt.show()

#Ring Pie Chart Method 1
plt.pie(x,labels=y,radius=1.5)
plt.pie([1],colors="w")
plt.legend()
plt.show()

#Ring Pie Chart Method 2
plt.pie(x,labels=y,radius=1.5)
cr = plt.Circle(xy=(0,0),radius=1,facecolor="w")
plt.gca().add_artist(cr)
plt.legend()
plt.show()