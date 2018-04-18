import numpy as np
import matplotlib.pyplot as pl

data = np.genfromtxt('data/iris.csv', delimiter=',')

petl = data[:,0]
petw = data[:,1]
sepl = data[:,2]
sepw = data[:,3]

pl.hist(petl)
pl.hist(petw)
pl.hist(sepl)
pl.hist(sepw)

pl.show()
