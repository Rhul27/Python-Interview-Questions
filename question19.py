# TO check numbers given are twin prime number or not


# Twin prime numbers are pairs of prime numbers that have a difference of 2. 
# In other words, twin primes are two prime numbers that are adjacent to each other and 
# have no other prime numbers between them. For example, (3, 5), (11, 13), and (17, 19) 
# are all examples of twin prime pairs. Twin primes have been a subject of interest in number 
# theory due to their unique properties and patterns.


def Isprime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
if Isprime(num1) and Isprime(num2):
    if abs(num1-num2)==2:
        print("Number is twin prime number")
    else:
        print("Number is not twin prime number")
else:
    print("Number are not the prime number")