'''
append
extend
count
insert
pop
remove
'''
a=[124,234524,"sdg",25,"asfwg "]
b=["shyam","nandu","vishnu","harika"]
a.append("shyam")
a.extend([124,1234,23,3,35])# extends the characters contineously.
print(a)# adds at last site.
print(a.count(25))# counts how many numbers are present in the given data.
print(a.pop(3))# it prints the indexing number.3 indexes the 25.
#print(a.index(25))#it gives the indexing number.
print(a.remove(124))#removes the 124 without any indexing.
#looping:
for i in [124,234524,"sdg",25,"asfwg "]:
    print(i) #for loop.looping
a.insert(0,"shyam")# it adds the data at particular place. 0 is the insertion index, and what to add.

print(a[::1])# [124, 234524, 'sdg', 25, 'asfwg '] gives the list as it is.
print(a[::-1])# ['asfwg ', 25, 'sdg', 234524, 124] reverse the list.
print(a[:1])# [124] index value as 0.
print(a[:-1])#[124, 234524, 'sdg', 25] prints all the list items except -1 index.
print(a[:])# prints the entire set.
print(b.sort(reverse=True))#reverse the string.
print(a.sort())# cannot give with different types of data type. it needs only one data type either numbers or strings......etc.
print(b.count)