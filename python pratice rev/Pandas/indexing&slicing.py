import numpy as sn
import pandas as pnd

shyam=pnd.Series([1,2,3,4,5,6],['aa','bb','cc','dd','ee','ff'])
nandu=pnd.Series([3,4,5,6,7,8],['AA','BB','CC','DD','EE','FF'])
print('value of aa in shyam',shyam['aa'])#in shyam aa refers to 1,bb refers to 2.......etc.
#value of AA in shyam 1
print('value of DD in shyam',nandu['DD'])#in nandu AA refers to 3,BB refers to 4.......etc.
#value of DD in shyam 6
# print('value of ff in shyam',nandu['ff'])#key error
print('value of EE in shyam',nandu['EE'])

