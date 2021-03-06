#52167 Programming and Scripting
#Tom Mirrington 04/2018

#script to divide dataset into seperate lists of petal length, petal width, sepal length and sepal width

#declare lists
sepl = []
sepw = []
petl = []
petw = []

#open csv and append data to corresponding lists
with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      sepl.append(float(x[0]))
      sepw.append(float(x[1]))
      petl.append(float(x[2]))
      petw.append(float(x[3]))


#references
#52167 pset 3,5
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#http://archive.ics.uci.edu/ml/datasets/Iris
