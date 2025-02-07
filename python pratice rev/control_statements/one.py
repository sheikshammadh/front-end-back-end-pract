'''
syntax
if condition:
    statement
elif conditon :
    statement
else:
    statement
'''
a=0
if a==True:
    print("its a true")#1 its a true
elif a==False:
    print("its a false")#2 neutral
else:
    print("neutral")#0 its a false



if True:
    print("outer if")
    if True:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer if")
#outer if
#inner if


age=17
if age>18:
    print("you can vote")
elif age==18:
    print("you can vote")
else:
    print("ypu cannot vote")