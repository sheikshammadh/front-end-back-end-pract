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

#=========================================================================================
#for loop
for i in range(5):
    print(i)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#while loop:
count = 0
while count < 5:
    print(count)
    count += 1

# =================================================================================================
# jumping loops
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)


for i in range(5):
    if i == 3:
        continue  # Skip the iteration when i is 3
    print(i)


for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

#============================================================================================================================================================
# right or wrong?
a=134
b=134
if a<b:
    print("right")
elif  a==b: 
    print("wrong")
#=============================================================================
# positive or negative
a=-1
if a>0:
    print("positive")
elif a==0:
    print("zero")
else:
    print("negative")
#=============================================================================
# odd or even
a=1
if a%2==0:
    print("even")
else:
    print("odd")
#==============================================================================
# iterate prime numbers from 1 to 100
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            break   
    return True
for i in range(1,101):
    if is_prime(i):
        print(i)
#==============================================================================
# for loop for even numbers
for i in range(1,11):
    if i%2!=0:
        print(i)
#==============================================================================
# tables multiples:
a=1234567
for i in range(1,11):
    print(a,"*",i,"=",a*i)
#==============================================================================
def check_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%1==0:
            return False
            break
        return True
number=1234
if check_prime(number):
    print(number,"it is a prime")
else:
    print(number,"not a prime")    