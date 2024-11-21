import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [2,3,4,2,5,1]
plt.stem(x,y,linefmt=":",markerfmt="g*", 
         bottom=0,basefmt="b",label="python",orientation="horizontal")
         #use_line_collection=False)# gives different color to the liens 
plt.legend()
plt.show()

#: => used for dotted line #markerfmt="r*" here r* shows green color and symbol *