# #int:
# a=123
# print(type(a))#<class 'int'>

# #conv:
# v=13341
# print(float(v))#13341.0


# a=10
# b=20
# print(type(a),type(b))#<class 'int'> <class 'int'>


# #float

# a=34.3434
# print(type(a))#<class 'float'>

# #conv:
# w=123.14354
# print(int(w))#123

# #bool

# a=True
# b=False
# print(type(a),type(b))#<class 'bool'> <class 'bool'>

# print(True==1)#true
# print(False==0)#true
# print(True==0)#false
# print(False==1)#false


# #complex

# a=1344+123j #(first numb is real and the second is imaginary.)
# print(type(a))#<class 'complex'>


# '''
# data loss explicit type conversions
# no data loss implicit type conversions
# '''

# # s=int(input("enter the number:"))
# # n=float(input("enter the number:"))
# # S=s+n
# # print(S)


# # None type:
# def greet():
#     pass
# greet()
# print(greet())# None
# print(type(greet()))#<class 'NoneType'>

#the type function returns the datatype.
# a=13#int
# b=13.143#float
# c=True#bool
# d="shyam"#string
# e=122+124j#complex
# f=(1,3,24,5,52)#tuple
# g=[123,34,52,52]#list
# h={"eid":1,"ename":"shyam"}#dict
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))



# bytes_values=bytes([0,2,4,36,134,255])
# print(bytes_values)#\x00\x02\x04$\x86\xff'
# print(type(bytes_values))#<class 'bytes'>
# for values in bytes_values:
#     print(values)# values in the array.
                  
# a=bytes([10,20,30,40,50,60])
# b=bytearray([10,20,30,40,50,60,70,80])
# c=frozenset({10,20,30,30,40,40,40,50})

# print(type(a))#bytes
# print(type(b))#bytearray
# print(type(c))#frozenset

# a=bytes([10,20,30,40,50,60])
# for i in a:
#     print(i)
# b=bytearray([10,20,30,40,50,60,70,80])
# for i in b:
#     print(i)
# c=frozenset({10,20,30,30,40,40,40,50})
# for i in c:
#     print(i)

# a=None
# print(a)#None
# print(type(a))#none type

a='q'
b=''
print(a+b)
