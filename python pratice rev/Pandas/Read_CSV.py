import pandas as pnd
#df=pnd.read_csv('D:\Learn - Full Stack\practices,front end and back end\python pratice rev\Pandas\data.csv')
#print(df.to_string())#use of  in this context is primarily to display the entire DataFrame as a neatly formatted string, especially if you want to inspect or debug your data comprehensively.
#having larger Data Frames with many rows and cols, pandas only give sthe first 5 rows and last 5 rows.thats why we use str to print add data.
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
#printing without string():
#df=pnd.read_csv('D:\Learn - Full Stack\practices,front end and back end\python pratice rev\Pandas\data.csv')
# print(df)
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
# max_rows:
#print(pnd.options.display.max_rows)#60
#print(pnd.options.display.max_columns)#0
#pnd.options.display.max_rows=99#Increase the maximum number of rows to display the entire DataFrame:
#df=pnd.read_csv('D:\Learn - Full Stack\practices,front end and back end\python pratice rev\Pandas\data.csv')
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
