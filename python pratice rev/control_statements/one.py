# '''
# syntax
# if condition:
#     statement
# elif conditon :
#     statement
# else:
#     statement
# '''
# a=0
# if a==True:
#     print("its a true")#1 its a true
# elif a==False:
#     print("its a false")#2 neutral
# else:
#     print("neutral")#0 its a false



# if True:
#     print("outer if")
#     if True:
#         print("inner if")
#     else:
#         print("inner else")
# else:
#     print("outer if")
# #outer if
# #inner if


# age=17
# if age>18:
#     print("you can vote")
# elif age==18:
#     print("you can vote")
# else:
#     print("ypu cannot vote")

# #=========================================================================================
# #for loop
# for i in range(5):
#     print(i)


# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# #while loop:
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# # =================================================================================================
# # jumping loops
# for i in range(5):
#     if i == 3:
#         pass  # Placeholder for future code
#     else:
#         print(i)


# for i in range(5):
#     if i == 3:
#         continue  # Skip the iteration when i is 3
#     print(i)


# for i in range(5):
#     if i == 3:
#         break  # Exit the loop when i is 3
#     print(i)

# #============================================================================================================================================================
# # right or wrong?
# a=134
# b=134
# if a<b:
#     print("right")
# elif  a==b: 
#     print("wrong")
# #=============================================================================
# # positive or negative
# a=-1
# if a>0:
#     print("positive")
# elif a==0:
#     print("zero")
# else:
#     print("negative")
# #=============================================================================
# # odd or even
# a=1
# if a%2==0:
#     print("even")
# else:
#     print("odd")
# #==============================================================================
# # iterate prime numbers from 1 to 100
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#             break   
#     return True
# for i in range(1,101):
#     if is_prime(i):
#         print(i)
# #==============================================================================
# # for loop for even numbers
# for i in range(1,11):
#     if i%2!=0:
#         print(i)
# #==============================================================================
# # tables multiples:
# a=1234567
# for i in range(1,11):
#     print(a,"*",i,"=",a*i)
# #==============================================================================
# def check_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%1==0:
#             return False
#             break
#         return True
# number=1234
# if check_prime(number):
#     print(number,"it is a prime")
# else:
#     print(number,"not a prime")    
# ===============================================================================
# even or odd?
# num=10352.5
# if num%2==0:
#     print(num,'is even')
# else:
#     print(num,'is odd')
# ===============================================================================
# three digit number or not?
# num=int(input('Enter number:'))
# if num>100 and num<999:
#     print(num,'is a three digit number')
# else:
#     print(num,'is not a three digit number')
# ================================================================================


# for loop:
# eid=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for i in eid:
#     print(i)
# for i in eid:
    # print("hi")#prints hi 15 times.bcz of the length of the seq.eid.

# for i in range(2, 10,2):
#     print(i)
# i=7
# for i in range(1,11):
#     print(7,"*",i,"=",7*i)
# employee_name=['rahul','vinay','dhanush','manoj','kishan']
# i=0
# while i==0:
#     print(f"{employee_name}")
#     i=i+1
# start = 1
# end = 20
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(i)

# 100 to 51
# i=100
# while i>=51:
#     print(i)
#     i=i-1

i=1
while i<=100:
    print(i)
    i=i+1