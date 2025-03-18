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

# i=1
# while i<=100:
#     print(i)
#     i=i+1

# i=100
# while i>51:
#     print(i)
#     i=i-1

# i=100
# while i>0:
#     print(i)
#     i=i-1

# for i in range(1,101):
#     print(i,"sorry nana. iam sorry....")
'''
emp=[{'eid':1,'ename':'Izak','gender':'Male'},
{'eid':2,'ename':'Louella','gender':'Female'},
{'eid':3,'ename':'Carol','gender':'Bigender'},
{'eid':4,'ename':'Eustacia','gender':'Female'},
{'eid':5,'ename':'Francisco','gender':'Male'},
{'eid':6,'ename':'Wenda','gender':'Female'},
{'eid':7,'ename':'Griffin','gender':'Male'},
{'eid':8,'ename':'Diarmid','gender':'Genderqueer'},
{'eid':9,'ename':'Twila','gender':'Female'},
{'eid':10,'ename':'Torrin','gender':'Bigender'},
{'eid':11,'ename':'Odie','gender':'Male'},
{'eid':12,'ename':'Dulcie','gender':'Female'},
{'eid':13,'ename':'Elfie','gender':'Female'},
{'eid':14,'ename':'Arv','gender':'Male'},
{'eid':15,'ename':'Terence','gender':'Male'},
{'eid':16,'ename':'Dix','gender':'Female'},
{'eid':17,'ename':'Rubia','gender':'Female'},
{'eid':18,'ename':'Brent','gender':'Male'},
{'eid':19,'ename':'Rozanne','gender':'Female'},
{'eid':20,'ename':'Kain','gender':'Male'},
{'eid':21,'ename':'Curtice','gender':'Male'},
{'eid':22,'ename':'Woodie','gender':'Male'},
{'eid':23,'ename':'Eal','gender':'Male'},
{'eid':24,'ename':'Eugenie','gender':'Female'},
{'eid':25,'ename':'Marsh','gender':'Male'},
{'eid':26,'ename':'Kaitlin','gender':'Female'},
{'eid':27,'ename':'Mortimer','gender':'Male'},
{'eid':28,'ename':'Ranice','gender':'Female'},
{'eid':29,'ename':'Fairlie','gender':'Male'},
{'eid':30,'ename':'Nell','gender':'Female'},
{'eid':31,'ename':'Chick','gender':'Male'},
{'eid':32,'ename':'Gradey','gender':'Male'},
{'eid':33,'ename':'Cory','gender':'Male'},
{'eid':34,'ename':'Isabelle','gender':'Genderqueer'},
{'eid':35,'ename':'Daron','gender':'Male'},
{'eid':36,'ename':'Electra','gender':'Female'},
{'eid':37,'ename':'Janina','gender':'Female'},
{'eid':38,'ename':'Kerstin','gender':'Female'},
{'eid':39,'ename':'Winston','gender':'Male'},
{'eid':40,'ename':'Kyla','gender':'Female'},
{'eid':41,'ename':'Caryl','gender':'Female'},
{'eid':42,'ename':'Arney','gender':'Male'},
{'eid':43,'ename':'Portia','gender':'Female'},
{'eid':44,'ename':'Cherice','gender':'Female'},
{'eid':45,'ename':'Killian','gender':'Male'},
{'eid':46,'ename':'Reynolds','gender':'Agender'},
{'eid':47,'ename':'Lulu','gender':'Female'},
{'eid':48,'ename':'Mable','gender':'Female'},
{'eid':49,'ename':'Ashlen','gender':'Female'},
{'eid':50,'ename':'Gilli','gender':'Female'},
{'eid':51,'ename':'Tess','gender':'Non-binary'},
{'eid':52,'ename':'Linc','gender':'Male'},
{'eid':53,'ename':'Corabella','gender':'Female'},
{'eid':54,'ename':'Julina','gender':'Female'},
{'eid':55,'ename':'Betteann','gender':'Female'},
{'eid':56,'ename':'Edith','gender':'Female'},
{'eid':57,'ename':'Alexei','gender':'Genderfluid'},
{'eid':58,'ename':'Massimiliano','gender':'Male'},
{'eid':59,'ename':'Barnie','gender':'Male'},
{'eid':60,'ename':'Alvan','gender':'Male'},
{'eid':61,'ename':'Damaris','gender':'Female'},
{'eid':62,'ename':'Conant','gender':'Male'},
{'eid':63,'ename':'Teressa','gender':'Female'},
{'eid':64,'ename':'Virge','gender':'Male'},
{'eid':65,'ename':'Davita','gender':'Female'},
{'eid':66,'ename':'Marris','gender':'Female'},
{'eid':67,'ename':'Eldon','gender':'Male'},
{'eid':68,'ename':'Elliott','gender':'Male'},
{'eid':69,'ename':'Afton','gender':'Female'},
{'eid':70,'ename':'Roma','gender':'Male'},
{'eid':71,'ename':'Debera','gender':'Female'},
{'eid':72,'ename':'Roy','gender':'Male'},
{'eid':73,'ename':'Marj','gender':'Female'},
{'eid':74,'ename':'Jacklyn','gender':'Female'},
{'eid':75,'ename':'Farand','gender':'Non-binary'},
{'eid':76,'ename':'Duffy','gender':'Male'},
{'eid':77,'ename':'Bernadette','gender':'Female'},
{'eid':78,'ename':'Rochell','gender':'Female'},
{'eid':79,'ename':'Abel','gender':'Male'},
{'eid':80,'ename':'Filia','gender':'Female'},
{'eid':81,'ename':'Tadd','gender':'Male'},
{'eid':82,'ename':'Worthington','gender':'Male'},
{'eid':83,'ename':'Perceval','gender':'Male'},
{'eid':84,'ename':'Heddi','gender':'Female'},
{'eid':85,'ename':'Padraic','gender':'Male'},
{'eid':86,'ename':'Mick','gender':'Male'},
{'eid':87,'ename':'Sandy','gender':'Female'},
{'eid':88,'ename':'Teodora','gender':'Female'},
{'eid':89,'ename':'Marcella','gender':'Female'},
{'eid':90,'ename':'Malia','gender':'Female'},
{'eid':91,'ename':'Tate','gender':'Male'},
{'eid':92,'ename':'Neala','gender':'Female'},
{'eid':93,'ename':'Trescha','gender':'Female'},
{'eid':94,'ename':'Clare','gender':'Male'},
{'eid':95,'ename':'Teodor','gender':'Male'},
{'eid':96,'ename':'Stanislas','gender':'Male'},
{'eid':97,'ename':'Aviva','gender':'Female'},
{'eid':98,'ename':'Freeman','gender':'Male'},
{'eid':99,'ename':'Betta','gender':'Female'},
{'eid':100,'ename':'Cordula','gender':'Female'}]
for employee in emp:
    #print(employee['ename'])# prints enames
    #print(employee['eid'])#prints eid.
    #print(employee['gender'])#prints gender
    # if employee['gender']=='Male':
    #     print("id",employee['eid'],"name",employee['ename'])
    #  if employee['gender']=='Female':
    #     print("id",employee['eid'],"name",employee['ename'])
     if employee['gender']=='Male':
        print("id",employee['eid'],"name",employee['ename'])
'''






