import matplotlib.pyplot as plt
x = [10,20,30,40,50,60,120,130,200] #for making an outler (o) the value must range far away from the largest value and 
                            #if there are more than value ranging at similar distance from the largest value 
                            #then the box plot extends without showing outler eg:from 60 to 120,130 there 
                            #will be no outler but when it is from 130 to 260 then the outler would come
plt.boxplot(x,notch=True, #changes the shape
            vert=False, #makes it horizonta; oriented
            widths=0.8,label="python",patch_artist=True, #fills color in the box
            showmeans=True, #shows the mean point as a dot
            whis=0.5, #it sets a range after which to show an outler #you can increase the whis value to join the outler
            sym="g+", #to customize the outler we use sym
            boxprops=dict(color="r"), #gives color to the box border 
            capprops=dict(color="y"), #gives color to the max min vala part 
            whiskerprops=dict(color="m"), #gives color to the whisks (ie. the line from the box to max/min) 
            flierprops=dict(markeredgecolor="y")) #flier property ko change krta hai
plt.legend()
plt.show()

#Overlapping Box Plot
x1 = [40,20,30,10,70,60,50,130]
plt.boxplot(x,showmeans=True)
plt.boxplot(x1,showmeans=True)
plt.show()

#Separate Box Plot
y = [x,x1] #list
plt.boxplot(y,showmeans=True,label=["python","c"])
plt.show()