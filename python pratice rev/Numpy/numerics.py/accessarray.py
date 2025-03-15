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
e=sn.zeros((2,3))
#print(e)#[[0. 0. 0.]
#         [0. 0. 0.]] prints zeros(0) in 2 rows in 3 columns.

f=sn.ones((3,3))
#print(f)#[[1. 1. 1.]
#         [1. 1. 1.]
#         [1. 1. 1.]]prints ones(1) in 3 rows in 3 columns.

g=sn.ones((2,3,2))#prints 2 times 3 rows, 2 col
#print(g)
        # [[[1. 1.]
        #  [1. 1.]
        #  [1. 1.]]

        #  [[1. 1.]
        #   [1. 1.]
        #   [1. 1.]]]
h=sn.ones((3,3,2))#prints 3 times 3 rows, 2 col
#print(h)#[[[1. 1.]
      #    [1. 1.]
      #    [1. 1.]]

      #   [[1. 1.]
      #    [1. 1.]
      #    [1. 1.]]

        #   [[1. 1.]
        #    [1. 1.]
        #    [1. 1.]]]
i=sn.full((2,9),12)#prints 12 given number in 2 rows 9 columns
#print(i)#[[12 12 12 12 12 12 12 12 12]
#         [12 12 12 12 12 12 12 12 12]]

j=sn.random.rand(5,4)# prints random numbers in 5 rows 4 col
#print(j)#[[0.07535346 0.12475281 0.6087353  0.49640024]
      #   [0.02100942 0.72392564 0.88643458 0.51007259]
      #   [0.65554607 0.39581187 0.64630727 0.5043525 ]
      #   [0.82109153 0.959322   0.54256615 0.30080779]
      #   [0.63334363 0.26031202 0.60663554 0.97545005]]
k=sn.identity(5)# prints 5 rows and 5 col like below.
#print(k)#[[1. 0. 0. 0. 0.]
        # [0. 1. 0. 0. 0.]
        # [0. 0. 1. 0. 0.]
        # [0. 0. 0. 1. 0.]
        # [0. 0. 0. 0. 1.]]



#copy (for changing in the indexing place values bby copy method in different arrays )
# l=sn.array([1,2,3,4,5])
# b=l#[1 2 3 4 5]
# b[0]=10#[10  2  3  4  5]
# l
# print(l)#[10  2  3  4  5]

# l=sn.array([1,2,3,4,5])
# b=l.copy()
# b[0]=10#[10  2  3  4  5]
# l
# print(l)#[1 2 3 4 5]

# *(multiply) all calculations are done.(+,-,*,/,//,%,**)
# o=sn.array([21,23,34,4])
# m=o+3
# print(m)#[24 26 37  7]
# n=o*6
# print(n)#[126 138 204  24]

