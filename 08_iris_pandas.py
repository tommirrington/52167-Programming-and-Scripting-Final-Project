import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/iris.csv', sep=',', names= ['sepl','sepw','petl','petw','class'])

df.plot.scatter(x='petl', y='petw');

plt.show()












#References
#Python Data Science Essentials by Alberto Boschetti, Luca Massaron, Publisher: Packt Publishing, Release Date: April 2015, ISBN: 9781785280429
#http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb
#read csv - https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html