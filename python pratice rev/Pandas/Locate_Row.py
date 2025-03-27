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
#print(df)
'''
     shyam  nandu
1st      1      5
2nd      2      4
3rd      3      3
4th      4      2
5th      5      1
'''
#Locate named indexes:must use 'loc' attribute.
#print(df.loc['3rd'])
'''
shyam    3
nandu    3
Name: 3rd, dtype: int64
'''
#Load files into Data Frame:
df=pnd.read_csv('D:\Learn - Full Stack\practices,front end and back end\python pratice rev\Pandas\data.csv')
#print(df)
'''
          Duration  Pulse  Maxpulse  Calories
0    0          60    110       130     409.1
1    1          60    117       145     479.0
2    2          60    103       135     340.0
3    3          45    109       175     282.4
4    4          45    117       148     406.0
5    164        60    105       140     290.8
6    165        60    110       145     300.4
7    166        60    115       145     310.2
8    167        75    120       150     320.4
9    168        75    125       150     330.4
'''
df=pnd.read_csv('D:\Learn - Full Stack\practices,front end and back end\python pratice rev\Pandas\data.csv')
print(df)