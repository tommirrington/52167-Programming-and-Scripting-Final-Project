import numpy as np
import statistics as stats

#use numpy libraray to import csv file as an ndarray and assign variable for each vector

data = np.genfromtxt('data/iris.csv', delimiter=',')

sepl = data[:,0]
sepw = data[:,1]
petl = data[:,2]
petw = data[:,3]

#using numpy and stats libraries print and format results

print('\n\nSepal Length')
print('Min:          {0:.1f}'.format(np.min(sepl)))
print('Max:          {0:.1f}'.format(np.max(sepl)))
print('Mean:         {0:.5f}'.format(np.mean(sepl)))
print('Mode:         {0:.2f}'.format(stats.mode(sepl)))
print('Median:       {0:.2f}'.format(stats.median(sepl)))
print('Std Dev:      {0:.2f}'.format(stats.pstdev(sepl)))
print('Variance:     {0:.2f}\n'.format(stats.pvariance(sepl)))

print('\nSepal Width')
print('Min:          {0:.1f}'.format(np.min(sepw)))
print('Max:          {0:.1f}'.format(np.max(sepw)))
print('Mean:         {0:.2f}'.format(np.mean(sepw)))
print('Mode:         {0:.2f}'.format(stats.mode(sepw)))
print('Median:       {0:.2f}'.format(stats.median(sepw)))
print('Std Dev:      {0:.2f}'.format(stats.pstdev(sepw)))
print('Variance:     {0:.2f}\n'.format(stats.pvariance(sepw)))

print('\nPetal Length')
print('Min:          {0:.1f}'.format(np.min(petl)))
print('Max:          {0:.1f}'.format(np.max(petl)))
print('Mean:         {0:.2f}'.format(np.mean(petl)))
print('Mode:         {0:.2f}'.format(stats.mode(petl)))
print('Median:       {0:.2f}'.format(stats.median(petl)))
print('Std Dev:      {0:.2f}'.format(stats.pstdev(petl)))
print('Variance:     {0:.2f}\n'.format(stats.pvariance(petl)))

print('\nPetal Width')
print('Min:          {0:.1f}'.format(np.min(petw)))
print('Max:          {0:.1f}'.format(np.max(petw)))
print('Mean:         {0:.2f}'.format(np.mean(petw)))
print('Mode:         {0:.2f}'.format(stats.mode(petw)))
print('Median:       {0:.2f}'.format(stats.median(petw)))
print('Std Dev:      {0:.2f}'.format(stats.pstdev(petw)))
print('Variance:     {0:.2f}\n\n'.format(stats.pvariance(petw)))

#References
#https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt
#https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html
#https://docs.python.org/3/library/statistics.html#module-statistics

