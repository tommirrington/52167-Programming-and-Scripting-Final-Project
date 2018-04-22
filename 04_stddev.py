#52167 Programming and Scripting
#Tom Mirrington 04/2018

#script to calculate the standard deviation in each data field

#define lists for petal length, petal width, sepalk length, sepal width
petl = []
petw = []
sepl = []
sepw = []

#open data file and seperate lines into a list for each data field.  count number of data lines.
y = 0

with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      sepl.append(float(x[0]))
      sepw.append(float(x[1]))
      petl.append(float(x[2]))
      petw.append(float(x[3]))


      y = y + 1
########################################################################################################
# Sepal Length
# 1. Work out the Mean (the simple average of the numbers)

mean_sepl = sum(sepl) / y

# 2. Then for each number: subtract the Mean and square the result

k = 0

for i in range(len(sepl)):
    j = (sepl[i] - mean_sepl) ** 2

    k = k + j

# 3. Then work out the mean of those squared differences.
# 4. Take the square root of that and we are done!

sd_sepl = float(k / len(sepl)) ** (1/2.0)

print("The sepal length standard deviation is {0:.2f}".format(sd_sepl))
########################################################################################################
# Sepal Width
# 1. Work out the Mean (the simple average of the numbers)

mean_sepw = sum(sepw) / y

# 2. Then for each number: subtract the Mean and square the result

k = 0

for i in range(len(sepw)):
    j = (sepw[i] - mean_sepw) ** 2

    k = k + j

# 3. Then work out the mean of those squared differences.
# 4. Take the square root of that and we are done!

sd_sepw = float(k / len(sepw)) ** (1/2.0)

print("The sepal width standard deviation is {0:.2f}".format(sd_sepw))      
########################################################################################################
# Petal Length
# 1. Work out the Mean (the simple average of the numbers)

mean_petl = sum(petl) / y

# 2. Then for each number: subtract the Mean and square the result

k = 0

for i in range(len(petl)):
    j = (petl[i] - mean_petl) ** 2

    k = k + j

# 3. Then work out the mean of those squared differences.
# 4. Take the square root of that and we are done!

sd_petl = float(k / len(petl)) ** (1/2.0)

print("The petal length standard deviation is {0:.2f}".format(sd_petl))
########################################################################################################
# Petal Width
# 1. Work out the Mean (the simple average of the numbers)

mean_petw = sum(petw) / y

# 2. Then for each number: subtract the Mean and square the result

k = 0

for i in range(len(petw)):
    j = (petw[i] - mean_petw) ** 2

    k = k + j

# 3. Then work out the mean of those squared differences.
# 4. Take the square root of that and we are done!

sd_petw = float(k / len(petw)) ** (1/2.0)

print("The petal width standard deviation is {0:.2f}".format(sd_petw))
########################################################################################################

#References
#standard deviation https://www.mathsisfun.com/data/standard-deviation-formulas.html
#using python built in functions https://docs.python.org/3/library/functions.html
#https://stackoverflow.com/questions/9595135/how-to-calc-square-root-in-python