'''
finction defenetion
function call
'''

# def function():
#     print("hi")# no output bcz we are not called.


# def function():
#     print("hello")
# function()#hello
# function()#hello
# function()...........how many time we want we can invoke.
# =================================================================

# def shyam():
#     print("nandu")
#     print("had lunch?")
#     print("what you had?")
# shyam()#nandu
# shyam()#had lunch?
# shyam()#what had?
# shyam()#nandu
# shyam()#had lunch?.......etc.
# ======================================================================

# def nandu(a,b):
#     return (a+b)
# print(12,12)#12 12 dont adds bcz we didnt give the function name in print invocation.

# ===================================================================

# def add(a,b):
#     return(a+b)
# print(add(12,10))# adds the both numbers
# =====================================================================

# def functionname(a,b,c,d):
#     print("this is shyam",a,b,c,d)
# functionname(1,2,3,4)#this is shyam 1 2 3 4
# functionname(1,2,3,4)#this is shyam 1 2 3 4
# functionname(1,2,3,4)#this is shyam 1 2 3 4
# ====================================================================

# def functionname(a):here only one parameter
#     print("this is shyam",a) 
# functionname(1,2,3) here 3 arguments so it will give error.
# functionname(1,2,3)
# functionname(1,2,3)#TypeError: functionname() takes 1 positional argument but 3 were given
# ========================================================================

# def functionname(*a):#this "*" gives the values to all arguments.
#     print("this is shyam",a) 
# functionname(1,2,3) #this is shyam (1, 2, 3)
# functionname(a=1,b=2,c=3)
# functionname(1,2,3)

# def functionname(**a):#this "**" gives the values to all arguments.
#     print("this is shyam",a) 
# functionname(a=1,b=2,c=3)#this is shyam {'a': 1, 'b': 2, 'c': 3}
# ============================================================================

# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner()
# outer()
#output:
      #outer
      #inner
# =========================================================================

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)

# def shyam(*arguments):#(*Arguments) 
#     return
# print(1,2,3,4,5,6,7,8,90)

# *Arguments:
#    when we dont know how many argumentsshould be passed then we can use "* arguments".this one argument 
# can hold multiple values or data.

# def shyam(*arguments):#(*Arguments) 
#     return
# print(1,2,3,4,5,6,7,8,90)

# **keyword arguments:
#     when we dont know how many arguments should we take. then we can use **keywordArguments.
# def function(**keywordArguments):
#     print(keywordArguments)
# function(name="shyam", age=24, gender="male")

