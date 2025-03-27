import numpy as sn
import pandas as pnd

shyam=['a','b','c','d','e']
nandu=[123,1234,123456,1234567,2345678]
vishnu=sn.array([nandu])
harika={'f':10,'g':20,'h':30}
ganta=['shyam','nandu','harika','vishnu','venky']
# print('set',shyam)# ['a', 'b', 'c', 'd', 'e'] given string name+ values in the statements.
# print('list',nandu)#list [123, 1234, 123456, 1234567, 2345678]given string name+ values in the statements.
# print('array',vishnu)#array [[    123    1234  123456 1234567 2345678]]given string name+ values in the statements.
# print('amar',harika)#amar {'f': 10, 'g': 20, 'h': 30}given string name+ values in the statements.
# ==================================================================================================================================================================================
# Creating a series:
# print(pnd.Series(data=nandu))#it gives indexing and values in a series.
'''
0        123
1       1234
2     123456
3    1234567
4    2345678
dtype: int64
'''
#print(pnd.Series(data=nandu,index=shyam))#it gets data from nandu and index from shyam.
'''
a        123
b       1234
c     123456
d    1234567
e    2345678
dtype: int64
'''
#print(pnd.Series(nandu,shyam))# nandu value + shyam values as series.
'''
a        123
b       1234
c     123456
d    1234567
e    2345678
dtype: int64
'''
#print(pnd.Series(harika))#dict values as key------values 
'''
f    10
g    20
h    30
dtype: int64
'''
#print(pnd.Series(ganta,shyam))gangat data and shyam data
'''
a     shyam
b     nandu
c    harika
d    vishnu
e     venky
dtype: object
'''


