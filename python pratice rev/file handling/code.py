'''
file handling in python
'''
'''
modes:
    1.open
    2.read
    3.write
    4.close
'''

o=open('shyam.txt','r')
print(o.read())
o.close()# from the file "shyam.txt" hi hello has given.

o=open('shyam.txt','w')
print(o.write("em chesthinnav"))
'''
given output as 9. the count of characters. aadded the given text into the file
 and the existing file is gone.
'''
o.close()

o=open('shyam.txt','a')
print(o.write("shyam nandu"))
'''
the given text is appended.the previous content is also existing still.
'''
o.close()