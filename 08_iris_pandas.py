import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data into a pandas dataframe
iris_df = pd.read_csv('data/iris.csv', sep=',', names= ['sepl','sepw','petl','petw','class'])

#print to the terminal screen a preforatted pandas report
print('\n\nSepal Length')
print(iris_df.sepl.describe())

print('\n\nSepal Width')
print(iris_df.sepw.describe())

print('\n\nPetal Length')
print(iris_df.petl.describe())

print('\n\nPetal Width')
print(iris_df.petw.describe())

##plt.figure(1, figsize=(10, 6), dpi=120, facecolor='w', edgecolor='k')
#using seaborn library print a facet grid scatter plot of petal width to petal length and 
#sepal width to sepal length

g = sns.FacetGrid(iris_df, hue="class")
g.map(plt.scatter, "sepl", "sepw") 
g.add_legend()

f = sns.FacetGrid(iris_df, hue="class")
f.map(plt.scatter, "petl", "petw") 
f.add_legend()
plt.show()

#References
#Python Data Science Essentials by Alberto Boschetti, Luca Massaron, Publisher: Packt Publishing, Release Date: April 2015, ISBN: 9781785280429
#http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb
#read csv - https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
#http://shichaoji.com/2017/02/16/famous-iris-dataset-visualization/
#seaborn pair plot - https://seaborn.pydata.org/tutorial/distributions.html
# facetgrid plot - https://seaborn.pydata.org/generated/seaborn.FacetGrid.html