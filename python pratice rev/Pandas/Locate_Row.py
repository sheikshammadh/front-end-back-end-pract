import pandas as pnd
#locate Row:
data={"shyam":[1,2,3,4,5],"nandu":[5,4,3,2,1]}
#df=pnd.DataFrame(data)
#print(df.loc[1])#locates the data at the index place '1'.
'''
shyam    2
nandu    4
Name: 1, dtype: int64
'''
#print(df.loc[[1,2,3]])#using a row of indexes.for multiple indexes we use two sqr brackets.
'''
   shyam  nandu
1      2      4
2      3      3
3      4      2
'''
#giving a each row name:
df=pnd.DataFrame(data,index=['1st','2nd','3rd','4th','5th'])
print(df)
'''
     shyam  nandu
1st      1      5
2nd      2      4
3rd      3      3
4th      4      2
5th      5      1
'''