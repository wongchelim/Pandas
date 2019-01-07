data = {'Name':pd.Series(['Apple','Xiaomi','Samsung','Google','Huawei','Sony','Jack']),
   'Founded':pd.Series([1981,1990,1998,1999,1981,1999,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
   
data2 = {'Name':pd.Series(['Apple','GIGI','Samsung','Xbox','Huawei','Sony','Bean','Long']),
   'Founded':pd.Series([1981,1993,1998,2002,1981,1999,50,90]),
   'Rating':pd.Series([4.23,5,3.98,4,3.20,4.6,9,10])}

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

print "dataframe 1"
print df1
print " "
print " "
print "dataframe 2"
print df2
print " "
print " "
print "dataframe reindex"
print df2.reindex_like(df1)
>>> print df2.reindex_like(df1)
   Founded     Name  Rating
0     1981    Apple    4.23
1     1993     GIGI    5.00
2     1998  Samsung    3.98
3     2002     Xbox    4.00
4     1981   Huawei    3.20
5     1999     Sony    4.60
6       50     Bean    9.00


>>> print df1.reindex_like(df2)
   Founded     Name  Rating
0   1981.0    Apple    4.23
1   1990.0   Xiaomi    3.24
2   1998.0  Samsung    3.98
3   1999.0   Google    2.56
4   1981.0   Huawei    3.20
5   1999.0     Sony    4.60
6     23.0     Jack    3.80
7      NaN      NaN     NaN


#reindex the columns 

>>> df2.reindex(columns=['Name', 'Rating'])
      Name  Rating
0    Apple    4.23
1     GIGI    5.00
2  Samsung    3.98
3     Xbox    4.00
4   Huawei    3.20
5     Sony    4.60
6     Bean    9.00
7     Long   10.00
>>> df2.reindex(columns=['Name', 'Rating2'])
      Name  Rating2
0    Apple      NaN
1     GIGI      NaN
2  Samsung      NaN
3     Xbox      NaN
4   Huawei      NaN
5     Sony      NaN
6     Bean      NaN
7     Long      NaN
