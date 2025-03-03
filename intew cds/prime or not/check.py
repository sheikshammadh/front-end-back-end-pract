number=int(input("Enter the Number:"))
if number<=1:
    print(number,"is not a prime")
else:
    for i in range(2,number):
        if (number % i)==0:
            print(number,"is not prime number")
            break
    else:
        print(number,"is a prime")

