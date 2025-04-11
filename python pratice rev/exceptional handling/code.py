'''
when an error occurs, python will normally stop  adn generate an error meaasage
these exception errors can be handled by the try statement
wwe will handle by using exceptional handling
''' 

a=10
# print(c)error.c is not defined
try:
    print(a)# risky code(it has error so this is not executed)
except:
    print("error")#error
else:
    print("no error") #it has error so this is not executed
finally:
    print("always")# always


a="shyam"
try:
    print("a")# risky code.
except:
    print("error")
else:
    print("no error") 
finally:
    print("always")
# here no error so the else, and finally will handle. then it gives "a","no error","always".

try:
    print( 's'+346)
except TabError:
    print("type error")
except ValueError:
    print("value error")

# it will gives as TypeError