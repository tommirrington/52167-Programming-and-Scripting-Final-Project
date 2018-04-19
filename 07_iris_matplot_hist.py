import numpy as np
import matplotlib.pyplot as plt

#use numpy libraray to import csv file as an array and assign variable for each vector

data = np.genfromtxt('data/iris.csv', delimiter=',')

sepl = data[:,0]
sepw = data[:,1]
petl = data[:,2]
petw = data[:,3]

#using matplotlib.pyplot output a figure consisrting of 4 formatted histogram subplots

plt.figure(1, figsize=(10, 6), dpi=120, facecolor='w', edgecolor='k')
plt.subplot(221)
plt.hist(sepl, color='g')
plt.xlabel('Length (cm)', fontsize=5)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title('Sepal Length', fontsize=10)
plt.grid(False)

plt.subplot(222)
plt.hist(sepw, color='b')
plt.xlabel('Length (cm)', fontsize=5)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title('Sepal Width', fontsize=10)
plt.grid(False)

plt.subplot(223)
plt.hist(petl, color='r')
plt.xlabel('Length (cm)', fontsize=5)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title('Petal Length', fontsize=10)
plt.grid(False)

plt.subplot(224)
plt.hist(petw, color='y')
plt.xlabel('Length (cm)', fontsize=5)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title('Petal Width', fontsize=10)
plt.grid(False)

plt.subplots_adjust(bottom=0.05, right=0.95, left=0.05, top=0.95, wspace=0.2, hspace=0.2)
plt.show()



#References
#https://matplotlib.org/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
#Working with multiple figures and axes - https://matplotlib.org/users/pyplot_tutorial.html
#set figure size - https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#label text size - https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#https://matplotlib.org/1.3.0/examples/pylab_examples/histogram_demo_extended.html