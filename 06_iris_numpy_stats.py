import numpy as np
import statistics as stats

data = np.genfromtxt('data/iris.csv', delimiter=',')

petl = data[:,0]
petw = data[:,1]
sepl = data[:,2]
sepw = data[:,3]

print('\n\nPetal Length')
print('Max:          {0:.1f}'.format(np.max(petl)))
print('Min:          {0:.1f}'.format(np.max(petl)))
print('Mean:         {0:.5f}'.format(np.mean(petl)))
print('Mode:         {0:.5f}'.format(stats.mode(petl)))
print('Median:       {0:.5f}'.format(stats.median(petl)))
print('Std Dev:      {0:.5f}'.format(stats.pstdev(petl)))
print('Variance:     {0:.5f}\n'.format(stats.pvariance(petl)))

print('\nPetal Width')
print('Max:          {0:.1f}'.format(np.max(petw)))
print('Min:          {0:.1f}'.format(np.max(petw)))
print('Mean:         {0:.5f}'.format(np.mean(petw)))
print('Mode:         {0:.5f}'.format(stats.mode(petw)))
print('Median:       {0:.5f}'.format(stats.median(petw)))
print('Std Dev:      {0:.5f}'.format(stats.pstdev(petw)))
print('Variance:     {0:.5f}\n'.format(stats.pvariance(petw)))

print('\nSepal Length')
print('Max:          {0:.1f}'.format(np.max(sepl)))
print('Min:          {0:.1f}'.format(np.max(sepl)))
print('Mean:         {0:.5f}'.format(np.mean(sepl)))
print('Mode:         {0:.5f}'.format(stats.mode(sepl)))
print('Median:       {0:.5f}'.format(stats.median(sepl)))
print('Std Dev:      {0:.5f}'.format(stats.pstdev(sepl)))
print('Variance:     {0:.5f}\n'.format(stats.pvariance(sepl)))

print('\nSepal Width')
print('Max:          {0:.1f}'.format(np.max(sepw)))
print('Min:          {0:.1f}'.format(np.max(sepw)))
print('Mean:         {0:.5f}'.format(np.mean(sepw)))
print('Mode:         {0:.5f}'.format(stats.mode(sepw)))
print('Median:       {0:.5f}'.format(stats.median(sepw)))
print('Std Dev:      {0:.5f}'.format(stats.pstdev(sepw)))
print('Variance:     {0:.5f}\n\n'.format(stats.pvariance(sepw)))



#https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt
#https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html
#https://docs.python.org/3/library/statistics.html#module-statistics

