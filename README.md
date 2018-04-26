# 52167-Programming-and-Scripting-Final-Project
Final project submission for the 52167 Programming and Scripting on the GMIT Higher Diploma in Data Analytics 2018 Course


## Notes and Ideas

* use python scripts to produce a report of the data set that can be used for similar data sets.  Output mean, median, mode, Max, Min

* Research [Math](https://docs.python.org/3/library/math.html#module-math) and [statistics](https://docs.python.org/3/library/statistics.html#module-statistics)  libraries to use existing functions 

* use numpy and matplotlib as per lecture

* investigate use of pandas

* Research [matplotlib](https://matplotlib.org/#) for producing graphs Mak

* install as Matplotlib.py, ana(conda) is not a framework install of ptython so follow specific instructions

* create similar outpur, formatted into columns with headers https://www.safaribooksonline.com/library/view/python-data-science/9781785280429/ch03.html


## Scripts
1. 01_seperate_data_fields.py - used to seperate iris data set input into seperate lists: petal length; petal width; sepal length; sepal width

1. 02_max_min.py - calculates the maximum and minimum values of: petal length; petal width; sepal length; sepal width

1. 03_mean.py - calculates the mean values of: petal length; petal width; sepal length; sepal width

1. 04_stddev.py - calculates the standard deviation of each dat field

1. 05_iris_combined_stats.py - script using only python basic functions to report max, min, mean and standard deviation

## Text

The iris data set is a data base that has been made available for use as a test case for data analytics studies and investigations.  The set comprises 150 data points representing the attributes recorded in samples of three classes of Iris flowers.  The data is used extensively in data analytics as a test case for many different applications from machine learning to graphical representation (2).  This paper will provide a detailed description of the data set, discuss the applications and its advantages and provide some exploratory analysis of the data using python scripts.

Description of iris flowers.


¬¬The Iris Flower Data set was created by Dr Edgar Anderson as part of his botanical studies into “The irises of the Gaspe Peninsula” and “The species problem in Iris” between 1935 and 1936 (3).  The information was then  made famous as a data set  by the eminent statistician Ronald Fisher in his 1936 paper “The Use of Multiple Measurements in taxonomic Problems”.  In this paper Fisher investigated ways in which Irises can be classified by their measurements and the linear relationships between those measurements.  He was successful in doing this and developed a linear discriminant model which was able to identify a class of iris from its measurements (4).

The data set consists of 150 data points separated into three sets of 50 by their species or class; iris – setosa, iris – virginica and iris – versicolor.  Each data point comprises four measurements; the sepal length, the sepal width, the petal length and the petal width.  The data set provides a good test case for data analytics as one class is linearly separable from the other two and those two are not linearly separable from each other (1).





Scripts 01 to 05 use basic functions only to report various statistics on the data set.  The basis of these calculations is script 01 which performs an operation to create independent lists of the data fields.  The lists are declared and the append function is used to separate the data into sepal length, sepal width, petal length and petal width.  The lists are all indexed in the same way so data fields will correspond with each other.  Script 02 uses the python built in functions to calculate and report the max and min for each data field.  Script 03 includes a counter to keep a running total on the number of data fields in the data set.  This is then used with the built in sum function to calculate the mean, this is reported using the print function and rounded to 2 decimal places to match the published results.  Script 04 is used to calculate the standard deviation.  The data is imported and separated into lists, the first step is to calculate the mean for each list or data field, a for loop is then used to iterate through the list calculating the difference between each measurement and the mean, these differences are squared and a running total is calculated using the k and j variables.  The calculated total of the squared differences is divided by the number of fields and the square root calculated.  An integer value is returned so the float declaration is used in the calculation to  maintain precision.  The result is printed to the terminal screen and formatted to two decimal places.  The final script using basic functions only combines all scripts 01 to 04 to produce a statistical report for each data field.  In this case though the mean and standard deviation have been declared as functions and the calculations made as part of the print steps.  This greatly reduces the amount of code needed to calculate and report the statistics.






1. https://www.safaribooksonline.com/library/view/python-data-science/9781785280429/ch01s04.html

Python Data Science Essentials
by Alberto Boschetti; Luca Massaron
Published by Packt Publishing, 2015

Chapter 1 : introducing ipython includes and explanation of the data set and its advantage

2. https://www.safaribooksonline.com/library/view/data-mining-with/9781785885716/ 
Data Mining with Python: Implementing Classification and Regression
  1 REVIEW
by James Church
Publisher: Packt Publishing
Release Date: July 2016
ISBN: 9781785885716

3. https://en.wikipedia.org/wiki/Ronald_Fisher

4. http://archive.ics.uci.edu/ml/datasets/Iris

1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica


review papers, also mention that one class is linearly seperable

good description and check stats http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names

http://academic.bancey.com/plotting-multivariate-data-with-matplotlibpylab-edgar-andersons-iris-flower-data-set/