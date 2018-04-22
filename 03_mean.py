#52167 Programming and Scripting
#Tom Mirrington 04/2018

#script to divide dataset into seperate lists of petal length, petal width, sepal length and sepal width

#declare lists
sepl = []
sepw = []
petl = []
petw = []

#use y as a counter to iterate through data set and provide a total
y = 0

#open csv and append data to corresponding lists
with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      sepl.append(float(x[0]))
      sepw.append(float(x[1]))
      petl.append(float(x[2]))
      petw.append(float(x[3]))

      #count number of data lines
      y = y + 1

#using python built in functions https://docs.python.org/3/library/functions.html calculate the mean using the sum function

mean_sepl = sum(sepl) / y
mean_sepw = sum(sepw) / y
mean_petl = sum(petl) / y
mean_petw = sum(petw) / y

#print mean values rounding to 1 d.p
#uncertain why print function produces error when () are used

print'The mean sepal length is', round(mean_sepl,2)
print'The mean sepal width is', round(mean_sepw,2)
print'The mean petal length is', round(mean_petl,2)
print'The mean petal width is', round(mean_petw,2)


#references
#52167 pset 3,5
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#https://docs.python.org/3/library/functions.html