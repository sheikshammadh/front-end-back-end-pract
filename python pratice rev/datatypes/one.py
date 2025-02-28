#int:
a=123
print(type(a))#<class 'int'>

#conv:
v=13341
print(float(v))#13341.0


a=10
b=20
print(type(a),type(b))#<class 'int'> <class 'int'>


#float

a=34.3434
print(type(a))#<class 'float'>

#conv:
w=123.14354
print(int(w))#123

#bool

a=True
b=False
print(type(a),type(b))#<class 'bool'> <class 'bool'>

print(True==1)#true
print(False==0)#true
print(True==0)#false
print(False==1)#false


#complex

a=1344+123j
print(type(a))#<class 'complex'>


'''
data loss explicit type conversions
no data loss implicit type conversions
'''

s=int(input("enter the number:"))
n=float(input("enter the number:"))
S=s+n
print(S)


