import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [2,4,6,8]

plt.bar(x,y)
plt.show()

c = ["r","y","g","b"]
plt.bar(x,y,color=c)
plt.show()

#combined graph
a = ["python","C","C++","Java"]
b = [85,70,60,82]
c = [20,30,40,50]
width = 0.5
plt.xlabel("language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("Data",fontsize=15)
plt.bar(a,b,width,color="g",align="center", #to align python,c,c++,java in center or can also use align="edge"
        edgecolor="b", #makes an outline around the bars of bar graph
        linewidth=5, #thickness of the outline
        linestyle=":", #makes the outline dotted
        alpha=0.5, #aplha parameter used to make the line transperant
        label="pop") #gives a label box
plt.bar(a,c,width,color="y",
        edgecolor="b",
        linewidth=5,
        linestyle=":", 
        alpha=0.5,
        label="pop1")
plt.legend(loc="best") #used to show the label (ie. popularity) without this command the lebel won't be shown
plt.show()

#separate graphs
d = ["python","C","C++","Java"]
e = [85,70,60,82]
f = [20,30,40,50]
p = np.arange(len(x))
width0 = 0.2
p1 = [j+width0 for j in p]
plt.xlabel("language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("Data",fontsize=15)
plt.bar(p,e,width0,color="g",align="center", #to align python,c,c++,java in center or can also use align="edge"
        edgecolor="b", #makes an outline around the bars of bar graph
        linewidth=5, #thickness of the outline
        linestyle=":", #makes the outline dotted
        alpha=0.5, #aplha parameter used to make the line transperant
        label="popularity") 
plt.bar(p1,f,width0,color="y",
        edgecolor="b",
        linewidth=5,
        linestyle=":", 
        alpha=0.5,
        label="popularity1")
plt.xticks(p+width/2,d,rotation=20) #to show python,C,C++,Java also #p+width/2 = used to show python,C,C++,Java in the center of both bars
plt.legend() #used to show the label (ie. popularity) without this command the lebel won't be shown
plt.show()

#to form a horizontal bar graph (use plt.barh())
g = ["python","C","C++","Java"]
h = [85,70,60,82]
i = [20,30,40,50]
width1 = 0.4
plt.xlabel("language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("Data",fontsize=15)
plt.barh(d,e,width1,color="g", #barh makes the bargraph horizontal
        edgecolor="b",
        linewidth=5,
        linestyle=":",
        alpha=0.5,
        label="popularity") 
plt.barh(d,f,width1,color="y",
        edgecolor="b",
        linewidth=5,
        linestyle=":", 
        alpha=0.5,
        label="popularity1")
plt.legend()
plt.show()
