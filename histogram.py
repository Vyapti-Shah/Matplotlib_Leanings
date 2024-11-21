import matplotlib.pyplot as plt
import numpy as np
import random

x = np.random.randint(10,60,(50)) #data between 10 to 60 and there should be 50 datas
print(x)

no = [42, 14, 41, 15, 21, 34, 51, 30, 34, 14, 48, 30, 14, 44, 59, 24, 28, 16, 29, 40, 48, 17, 44, 56,
      20, 59, 21, 23, 42, 32, 54, 28, 41, 22, 35, 10, 42, 45, 18, 48, 35, 27, 34, 15, 24, 19, 15, 24,
      50, 41]
l = [10,20,30,40,50,60]

#Solid Histogram
plt.hist(no,color="b",edgecolor="g", alpha=0.6, label="set",
        cumulative=-1, #cumultive=-1 used to reverse the bar chart
        bottom=10, #bottom=10 is used when to start the y-axis count from 10 and not 0
        align="mid",
        rwidth=0.8) #width of one bar
plt.title("data")
plt.xlabel("python")
plt.ylabel("No.")
plt.grid()
plt.axvline(32,color="g",label="line") #shows that the graph is divided into 2 parts right hand side and left hand side
plt.show()

#Step Historgam
plt.hist(no,edgecolor="b", alpha=0.6, histtype="step", #histtype maybe stepfilled, barstackked, bar
         orientation="horizontal",label="set") 
plt.title("data")
plt.xlabel("python")
plt.ylabel("No.")
plt.show()

#log value on y aixs
plt.hist(no,edgecolor="b", alpha=0.6, histtype="step", #histtype maybe stepfilled, barstackked, bar
         log=True,label="set") 
plt.title("data")
plt.xlabel("python")
plt.ylabel("No.")
plt.show()