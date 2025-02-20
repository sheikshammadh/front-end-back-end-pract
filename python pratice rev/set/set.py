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
print(s2.issuperset(s1)) #This checks if all elements of s1 are also in s2. Since s2 contains 123 and 456 but does not contain 789, it returns False.
