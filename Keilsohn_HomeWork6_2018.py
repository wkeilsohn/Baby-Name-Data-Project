# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:03:28 2018

@author: William Keilsohn 
"""

# Import Relevant Packages:

import numpy as np
import pandas as pd
from titlecase import titlecase as tc #https://pypi.org/project/titlecase/

# Find the most common boys name in 1990:

# First going to have to import the baby data from 1990
names1900 = pd.read_csv('National Data\yob1900.txt', names = ['name', 'sex', 'births']) #Based off ppt.

# Sort out the boys
boys1900 = names1900[names1900.sex=='M'] #ppt

# Print out the number 1 name
print("The most common boy's name in 1900 was:")
print(boys1900.iloc[0][0]) #Answers the question
print('\n') #I just like a little extra space

# Accept a name from the counsole
name = input("Please enter a name: ")
name = tc(name) #All the names in the registry are titlecase

# Obtain the rest of the data
years = range(1880,2018) #It's a range, so the last digit is exclusive
pieces = []
columns = ['name','sex','births']
for year in years:   
    path = 'National Data/yob%d.txt' %year   
    frame = pd.read_csv(path,names=columns)    
    frame['year'] = year
    pieces.append(frame) 
nameData = pd.concat(pieces, ignore_index=True) #from ppt


# Determine what year that name was most popular
birthPivot = nameData.pivot_table('births', index = 'year', columns = 'name', aggfunc = sum) #ppt
plotData = birthPivot[[name]]
orderData = plotData.sort_values(by = name, ascending = False) #ppt
print("The year the name ")
print(name)
print("was most common, was: ")
print(orderData[name].index.values[0]) #https://stackoverflow.com/questions/17241004/pandas-how-to-get-the-data-frame-index-as-an-array
#Answers question

# Print out a chart of that name over time
plotData.plot(subplots = True, figsize = (12, 10), grid = True, title = 'Number of Births per Year')# ppt
#Answers question
#Also I wanted the grid. I think it makes the plot easier to read.

# Take a year as input
Year = input("Please enter a year: ") #Not sure why it demands the year before it plots
Year = int(Year)

# Print out the top 25 boys and girls names of that year
def sexPrinter(string):
    DataSub = nameData[nameData.sex == string]
    DataPivot = DataSub.pivot_table('births', index = 'name', columns = 'year', aggfunc = sum)
    DataYear = DataPivot[[Year]]
    DataOrder = DataYear.sort_values(by = Year, ascending = False)
    print('In the year')
    print(Year)
    if string == 'M':
        print("The top 25 boy's names were: ")
    else:
        print("The top 25 girl's names were: ")
    print(DataOrder[Year].index.values[0:25]) #https://stackoverflow.com/questions/17241004/pandas-how-to-get-the-data-frame-index-as-an-array
    print('\n')

sexPrinter('F')
sexPrinter('M') #Answers question