#copy (for changing in the indexing place values bby copy method in different arrays )
l=sn.array([1,2,3,4,5])
b=l#[1 2 3 4 5]
b[0]=10#[10  2  3  4  5]
l
print(l)#[10  2  3  4  5]

l=sn.array([1,2,3,4,5])
b=l.copy()
b[0]=10#[10  2  3  4  5]
l
print(l)#[1 2 3 4 5]