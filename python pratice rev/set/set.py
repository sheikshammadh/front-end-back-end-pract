a={1,2,234,545,13434,4}
# print(type(a))
# print(a)
'''
add
update
pop
remove
'''
#a.add("shyam")
#print(a)#add in the random palces.

# a.update({1,2,3,4,5})# updates the values with the values in a row.
# print(a)

# a.pop()# pop a random value
# print(a)

# a.remove(234)# removes the specified value.
# print(a)

'''
union
intersect
difference
issubset
issuperset
'''
s1={123,456,789}
s2={123,456,678,345,12345}
#print(s1.union(s2))# prints all the values in one set.
#print(s1.intersection(s2))#prints common in two sets.
#print(s1.difference(s2))#789 This prints the elements that are in s1 but not in s2. The result would be {789}.
#print(s1.issubset(s2))false This checks if all elements of s1 are also in s2. Since 789 is not in s2, it returns False.
#print(s2.issubset(s1))false This checks if all elements of s2 are also in s1. Since 678, 345, and 12345 are not in s1, it returns False.
#print(s1.issuperset(s2))false This checks if all elements of s2 are also in s1. Since s1 does not contain 678, 345, or 12345, it returns False.
#print(s2.issuperset(s1)) #This checks if all elements of s1 are also in s2. Since s2 contains 123 and 456 but does not contain 789, it returns False.


# s1={'a','b','c','d'}
# s2={'e','f','g','h'}
# s1.update('z')
# print(s1)


# s1={10,20,30,40}
# s2={20,30,40,50}
# s1.update('z')
# s1.add(90)
# # print(s1)
# s1.add(s2)
# print(s1)#TypeError: unhashable type: 'set'

# s1={'a','b','c','d'}
# s2={'e','f','g','h'}
# s3='shyam'
# s1.update('z')
# # print(s1)
# s1.update(s3)
# #print(s1)#{'b', 'y', 'z', 'c', 's', 'h', 'm', 'd', 'a'} every letter comes as string.
# print()

# s1={'a','b','c','d'}
# s2={'e','f','g','h'}
# s1.remove('a')
# print(s1)#{'b', 'd', 'c'}
# s1.discard('b')
# print(s1)#{'a', 'd', 'c'}
# s1.clear()
# print(s1)#set() empty set.
# s1.pop()
# print(s1)#{'d', 'c', 'b'} 'a' removed
# s2.pop()
# print(s2)#{'h', 'e', 'f'}
# s1.remove('z')
# print(s1)# key error:'z' gives error.
# s1.discard('z')
# print(s1)#{'d', 'c', 'a', 'b'} dont gives the error.

s1={10,20,30,40}
s2={30,40,50,60}
# print(s1.union(s2))#{40, 10, 50, 20, 60, 30}
# print(s1.intersection(s2))#{40, 30}
# print(s1.difference(s2))#{10, 20}
# print(s1.symmetric_difference(s2))#{10, 50, 20, 60}
# print(s1+s2)#TypeError: unsupported operand type(s) for +: 'set' and 'set'.
# print(s1 and s2)#{40, 50, 60, 30}
# print(s1||s2)#SyntaxError: invalid syntax
# print(s1-s2)#{10, 20}
# print(s1^s2)#{10, 50, 20, 60}



# s1={10,20,30,40}
# s2={30,40,50,60}
# print(s1.issubset(s2))#False
# print(s2.issubset(s1))#False
