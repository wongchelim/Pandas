#!/usr/bin/python
#this is to demonstrate how the pandas dataframe looks like and how it work.
import pandas as pd
import numpy as np

#this will display the values of 1,2,3,4,5 with the column name 0 and row start with 0
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print df
print " "
print " "


#this will display the values of John with age col as 30 and so forth with the column name name and age with respective values
data = [['John',30],['Wong',36],['Danny',41]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df

print " "
print " "


#this will display the values of John with age col as 30 and so forth with the column name name and age with respective values
data = {'Name':['John', 'Wong', 'Danny', 'Ricky'],'Age':[30,36,41,44]}
df = pd.DataFrame(data)
print df

print " "
print " "

df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])

#this will display the values record by record inside the dict, if no values then it show NaN
data = [{'John': 1, 'Wong': 2},{'John': 5, 'Wong': 10, 'Danny': 20}]
#display the row(Y) values at the side. This require to be known how many records inside the data so it only show the value of the Y axis. Else it will error out.
df = pd.DataFrame(data, index=['Row1','Row2'])
#By now we have X-axis column values and Y-axis rows value.
print df

print " "
print " "
print " "

#Another table, but if you place another column name into the data dict wihtou data it will error out.
data = [{'John': 1, 'Wong': 2},{'John': 5, 'Wong': 10, 'Nicky': 20},{'Nicky': 50}]
df = pd.DataFrame(data, index=['first', 'second','third'])
print df

#        John  Nicky  Wong
#first    1.0    NaN   2.0
#second   5.0   20.0  10.0
#third    NaN   50.0   NaN

print " "
print " "
print " "

#Systematic way displaying data, in another words, but still need to specify the y-axis(indexes) with number of records
data = [{'Age': 1, 'Hobbies': 2},{'Age': 5, 'Hobbies': 10, 'Lover': 20},{'Age': 12}]
df2 = pd.DataFrame(data, index=['John', 'Wong','Nicky'], columns=['Age', 'Hobbies','Lover','Hater'])
print df2


#       Age  Hobbies  Lover  Hater
#John     1      2.0    NaN     NaN
#Wong     5     10.0   20.0     NaN
#Nicky   12      NaN    NaN     NaN

print " "
print " "
print " "


#Only select a specific column
print df2['Age']


#John      1
#Wong      5
#Nicky    12
#Name: Age, dtype: int64

#it is to add both columns together
print df2['Age']+df2['Hobbies']


#
#
#Add column
#
#

#this will craete a new column that add the both Age and hobbies
df2['weirdadd']=df2['Age']+df2['Hobbies']
print df2

#       Age  Hobbies  Lover  Hatter  weirdadd
#John     1      2.0    NaN     NaN       3.0
#Wong     5     10.0   20.0     NaN      15.0
#Nicky   12      NaN    NaN     NaN       NaN

print " "
print " "
print " "

#this will just craete a new column(newcol) with it values on each rows.
df2['newcol']=pd.Series([100,200,300],index=['John','Wong','Nicky'])
print df2

#       Age  Hobbies  Lover  Hatter  weirdadd  newcol
#John     1      2.0    NaN     NaN       3.0     100
#Wong     5     10.0   20.0     NaN      15.0     200
#Nicky   12      NaN    NaN     NaN       NaN     300

print " "
print " "
print " "

#
#
#Remove column
#
#

#remove a column using
# using del function
print ("Deleting the weirdadd column using DEL function:")
del df2['weirdadd']
print df2

#       Age  Hobbies  Lover  Hatter  newcol
#John     1      2.0    NaN     NaN     100
#Wong     5     10.0   20.0     NaN     200
#Nicky   12      NaN    NaN     NaN     300

print " "
print " "
print " "


# using pop function
print ("Deleting newcol column using POP function:")
df2.pop('newcol')
print df2


#       Age  Hobbies  Lover  Hatter
#John     1      2.0    NaN     NaN
#Wong     5     10.0   20.0     NaN
#Nicky   12      NaN    NaN     NaN

print " "
print " "
print " "


#
#
#Select specific row
#
#
#need to be a integer

print df2.iloc[1]

#Age        12.0
#Hobbies     NaN
#Lover       NaN
#Hatter      NaN



#
#Add row
#

#this will add a row of Angela and its value
df2.loc['Angela'] = [26, 6, 6,2]

#        Age  Hobbies  Lover  Hatter
#John      1      2.0    NaN     NaN
#Wong      5     10.0   20.0     NaN
#Nicky    12      NaN    NaN     NaN
#Angela   26      6.0    6.0     2.0

#it will ignore the index and replace them to integer with a new line added.

df2 = df2.append({'Age' : 50 , 'Hobbies' : 22,'Lover':6, 'Hatter' : 1} , ignore_index=True)
#   Age  Hobbies  Lover  Hatter
#0    1      2.0    NaN     NaN
#1    5     10.0   20.0     NaN
#2   12      NaN    NaN     NaN
#3   26      6.0    6.0     2.0
#4   50     22.0    6.0     1.0

#Conclusion avoid using indexes as a name.


#
#Remove a row
#

#it will drop the row by specifying the index name or the row number.
>>> print df2
      Age  Hobbies  Lover  Hatter
0       1      2.0    NaN     NaN
1       5     10.0   20.0     NaN
2      12      NaN    NaN     NaN
3      26      6.0    6.0     2.0
4      26      6.0    6.0     2.0
5      50     22.0    6.0     1.0
Baby   26      6.0    6.0     3.0
>>> df2 = df2.drop(3)
>>> print df2
      Age  Hobbies  Lover  Hatter
0       1      2.0    NaN     NaN
1       5     10.0   20.0     NaN
2      12      NaN    NaN     NaN
4      26      6.0    6.0     2.0
5      50     22.0    6.0     1.0
Baby   26      6.0    6.0     3.0
>>> df2 = df2.drop('Baby')
>>> print df2
   Age  Hobbies  Lover  Hatter
0    1      2.0    NaN     NaN
1    5     10.0   20.0     NaN
2   12      NaN    NaN     NaN
4   26      6.0    6.0     2.0
5   50     22.0    6.0     1.0
>>>
