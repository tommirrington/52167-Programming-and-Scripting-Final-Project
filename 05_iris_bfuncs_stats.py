#script combing scripts 01 -04 to output max, min, mean and standard deviation using 
#only python basic functions.

#define lists and input csv, write each line indec into a seperate list

petl = []
petw = []
sepl = []
sepw = []

y = 0

with open("data/iris.csv") as f:
    for line in f:
      x = line.split(',')
      sepl.append(float(x[0]))
      sepw.append(float(x[1]))
      petl.append(float(x[2]))
      petw.append(float(x[3]))


      y = y + 1

#define mean as a function, argument is a data list
def mean(a):

  b = sum(a) / len(a)

  return b

#define standard deviation as a function, argument is a data list
def stdev(c):

  mean_c = sum(c) / len(c)

  k = 0

  for i in range(len(c)):
      j = (c[i] - mean_c) ** 2

      k = k + j

  d = float(k / len(c)) ** (1/2.0)

  return d

print('\n\nSepal Length')
print('Min:          {0:.1f}'.format(min(sepl)))
print('Max:          {0:.1f}'.format(max(sepl)))
print('Mean:         {0:.2f}'.format(mean(sepl)))
print('Std Dev:      {0:.2f}\n'.format(stdev(sepl)))

print('\nSepal Width')
print('Min:          {0:.1f}'.format(min(sepw)))
print('Max:          {0:.1f}'.format(max(sepw)))
print('Mean:         {0:.2f}'.format(mean(sepw)))
print('Std Dev:      {0:.2f}\n'.format(stdev(sepw)))

print('\nPetal Length')
print('Min:          {0:.1f}'.format(min(petl)))
print('Max:          {0:.1f}'.format(max(petl)))
print('Mean:         {0:.2f}'.format(mean(petl)))
print('Std Dev:      {0:.2f}\n'.format(stdev(petl)))

print('\nPetal Width')
print('Min:          {0:.1f}'.format(min(petw)))
print('Max:          {0:.1f}'.format(max(petw)))
print('Mean:         {0:.2f}'.format(mean(petw)))
print('Std Dev:      {0:.2f}\n\n'.format(stdev(petw)))


#references
#52167 pset 3,5
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#https://docs.python.org/3/library/functions.html

