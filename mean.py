#script to divide dataset into seperate lists of petal length, petal width, sepal length and sepal width
#declare lists

petl = []
petw = []
sepl = []
sepw = []

#count number of data lines
y = 0

with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      petl.append(float(x[0]))
      petw.append(float(x[1]))
      sepl.append(float(x[2]))
      sepw.append(float(x[3]))

      y = y + 1

#using python built in functions https://docs.python.org/3/library/functions.html

mean_petl = sum(petl) / y
mean_petw = sum(petw) / y
mean_sepl = sum(sepl) / y
mean_sepw = sum(sepw) / y

#print mean values rounding to 1 d.p
#uncertain why print function produces error when () are used

print'The mean petal length is', round(mean_petl,1)
print'The mean petal width is', round(mean_petw,1)
print'The mean sepal length is', round(mean_sepl,1)
print'The mean sepal width is', round(mean_sepw,1)




#references
#52167 pset 3,5
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#https://docs.python.org/3/library/functions.html