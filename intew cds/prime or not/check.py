number=int(input("enter the value:"))
if number>1:
    for i in range(2, number):
        if (number % i):
            print(number,"number is not a prime")
    else:
        print(number,"is a prime number")
else:
    print(number,"not a prime number")