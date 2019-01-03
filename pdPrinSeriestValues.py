#!/usr/bin/python
#this is to demonstrate how the pandas series looks like and how it work.

import pandas as pd
import numpy as np

#if no index assigned(such as put in numpy array), it only serve as a list of city data
print "Simple series using array"
citydata = np.array(['KL','PJ','LD','NY'])
cityseries = pd.Series(citydata)
print cityseries
print " "
print " "

#if no index assigned(such as put in numpy array), it assign later into the panda series, it display a city list with their index(which know how to find them)
print "Simple series with indexes using array"
citydata = np.array(['KL','PJ','LD','NY'])
cityseries = pd.Series(citydata,index=[100,101,102,103])
cityseries2 = pd.Series(['KL','PJ','LD','NY'],index = [100,101,102,103])
cityseries3 = pd.Series(['KL','PJ','LD','NY'],index = ['a100','a101','a102','a103'])

print "Print the list contain"
print cityseries
print " "
print cityseries[0], "this is the first value"
print " "
print "Print the second list contain"
print cityseries2
print " "
#print cityseries2[0], "this will print out the error as there do not have any value inside the 0" as when index define as interger it assume all in interger
print cityseries2[101]
print " "
print cityseries3[0] #this will show everything the sequence as the indexes are in strings
print " "
print cityseries3['a102'], "the third value"
print " "
print cityseries3['a100','a101','a102'] #print the index value not exist will error out.
print " "
print " "

#if a only value is a scalar value, it assign later with list of index into the panda series, it display a repeatable same value as long as the indexes exits
print "Simple series with indexes using array if only 1 value but contain indexes."
cityseries = pd.Series(5, index=[100, 101, 102, 103])
print cityseries
print " "
print " "


print "Simple series with indexes using dict"
#if using dict(with curly bracket), it can assign value with index with it at one line.
citydata = {'KL' : 100., 'PJ' : 101., 'LD' : 102., 'NY' : 103}
cityseries = pd.Series(citydata)
print cityseries
print " "
print " "
