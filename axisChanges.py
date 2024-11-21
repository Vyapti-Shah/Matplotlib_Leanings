import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,1,4,2]
plt.plot(x,y)
#plt.xticks(x,labels=["python","c","c++","java"])
#plt.yticks(x) #to change the values shown in the respective axis
plt.xlim(0,10) #limits the x coordinates to be shown (x1,x2)
plt.ylim(0,10) #limits the y coordinates to be shown (y1,y2)
plt.show()

#limiting using axis() parameter
a = [1,2,3,4]
b = [3,1,4,2]
plt.plot(a,b)
plt.axis([0,10,0,7]) #([x1,x2,y1,y2])
plt.show()
