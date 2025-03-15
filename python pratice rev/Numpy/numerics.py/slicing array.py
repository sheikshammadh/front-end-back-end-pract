import numpy as sn
a=sn.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
#print(a)#[[1 2 3 4 5 6] column0
#         [1 2 3 4 5 6]] column1
b=a[1,2]  #                 ↑
#print(b)#3 in column1 index ↑ value 2 (3)
b=a[0,4]
#print(b)#5 in column0 index value 4 (5)
c=a[1,:]
#print(c)#[1 2 3 4 5 6] col-0 total row prints.
#print(c)#[1 2 3 4 5 6] col-1 total row prints
d=a[:,4]
#print(d)#[5 5] in both arrays index values of 4 value is 5,5
