import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1,2,3,4]
plt.subplot(2,2,1) #subplot(rows,columns,index)
plt.plot(x,y,color="g")

plt.subplot(2,2,2)
plt.pie([1],colors="g")

x1 = [10,20,30,40]
plt.subplot(2,2,3)
plt.pie(x1)

x2 = ["a","b","c","d"]
y2 = [10,20,30,40]
plt.subplot(2,2,4)
plt.bar(x2,y2)

plt.show()