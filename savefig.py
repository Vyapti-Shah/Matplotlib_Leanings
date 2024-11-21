import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,3,6,4]
plt.plot(x,y,color="g")
plt.savefig("line_savefig") #save the image of the graph in png format in the folder working on
plt.show()

a = [1,2,3,4,5]
b = [2,4,3,6,4]
plt.plot(a,b,color="g")
plt.savefig("line1_savefig", #save the image of the graph in png format (default) in the folder working on
            dpi=1000, #clears the view on zooming
            facecolor="y") #gives the background yellow color
plt.show()

c = [1,2,3,4,5]
d = [2,4,3,6,4]
plt.plot(c,d,color="g")
plt.savefig("line2_savefig.pdf") #save the image of the graph in pdf format in the folder working on
plt.savefig("line3_savefig.jpg") #save the image of the graph in jpg format in the folder working on
plt.show()

e = [1,2,3,4,5]
f = [2,4,3,6,4]
plt.plot(e,f,color="g")
plt.savefig("line4_transparent_savefig",facecolor="y",transparent=True,bbox_inches="tight")
plt.show()