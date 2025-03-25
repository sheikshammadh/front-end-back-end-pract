# import math
# print (math.pi)#3.141592653589793
# print (math.sqrt(64))#8.0
# print (math.ceil(9.8))#10
# print (math.floor(9.8))#9
# ====================================================================================================================
# from math import pi,sqrt,ceil,floor
# print (pi)#3.141592653589793
# print (sqrt(64))#8.0
# print (ceil(9.8))#10
# print (floor(9.8))#9
# =====================================================================================================================
# from math import*
# print (pi)#3.141592653589793
# print (sqrt(64))#8.0
# print (ceil(9.8))#10
# print (floor(9.8))#9
# =====================================================================================================================
# import random
# print(random.randint(10,99))#prints any number randomly.
# print(random.randrange(1,9))#prints any number randomly.
# ===================================================================================================================
# from random import randint
# for i in range(1,21):#prints 20 numbers
#     print(randint(10,99))# prints 20 numbers randomly from 10 to 99.
# ===================================================================================================================
from random import randint,choices
lottery_digits=[]
for i in range(10):
    lo