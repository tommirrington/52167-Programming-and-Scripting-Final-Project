
#script to divide dataset into seperate lists of petal length, petal width, sepal length and sepal width
#import math
#import statistics

petl = []
petw = []
sepl = []
sepw = []

with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      petl.append(float(x[0]))
      petw.append(float(x[1]))
      sepl.append(float(x[2]))
      sepw.append(float(x[3]))


#references
#52167 pset 3,5
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

