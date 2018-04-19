
#script to divide dataset into seperate lists of petal length, petal width, sepal length and sepal width
#import math
#import statistics

sepl = []
sepw = []
petl = []
petw = []

with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      sepl.append(float(x[0]))
      sepw.append(float(x[1]))
      petl.append(float(x[2]))
      petw.append(float(x[3]))

#using python built in functions https://docs.python.org/3/library/functions.html

print'The maximum sepal length is' ,max(sepl)
print'The maximum sepal width is' ,max(sepw)
print'The maximum petal length is' ,max(petl)
print'The maximum petal width is' ,max(petw)

print'The minimum sepal length is' ,min(sepl)
print'The minimum sepal width is' ,min(sepw)
print'The minimum petal length is' ,min(petl)
print'The minimum petal width is' ,min(petw)




#references
#52167 pset 3,5
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#https://docs.python.org/3/library/functions.html
