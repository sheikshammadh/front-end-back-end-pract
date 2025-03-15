import numpy as sn

a=sn.array([1,2,3,4,5])
# print(a)#[1 2 3 4 5]   1 dimensional array

# a=np.array([[1,2,3,4,5],[1,2,3,4,5,6]])
# print(a)
'''
[1, 2, 3, 4, 5] has 5 elements.

[1, 2, 3, 4, 5, 6] has 6 elements.

When numpy tries to create an array, it expects all nested lists (or rows, in this case) to have 
the same length so that it can form a consistent shape (e.g., 2x5, 2x6). If the lengths 
are mismatched, it results in a ValueError because the resulting array would be "inhomogeneous."
'''

b=sn.array([1,2,3])
#print(b)#[[1 2 3 4 5],
         #[1 2 3 4 5]]  #2 dimensional array
#dimensions
# it shows how many dimensions 1 or 2 or 3 or 4 or 5.......etc.
c=b.ndim
#print(c)#2
# shape
#shape shows the number of rows and columns present in the array.
d=b.shape
# print(d)#(2, 5)2 rows and 5 columns

#datatype
# it shows the datatype
e=b.dtype
#print(e)#int64

# size
f=b.itemsize
#print(f)#8

# bytes 1 item size is 4 bytes.
g=b.nbytes
#print(g)#24 1 digit*4. every digit is multiplied by 4.
h=sn.array([[[1,2,3],[3,4,5],[5,6,7]]])
i=h.ndim
print(i)#3 three lists of values so it is 3dimensional.