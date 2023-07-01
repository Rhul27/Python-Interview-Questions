# Factorial of the number 

# Method 1 :
import math
num=int(input("Enter the number : "))
fact=math.factorial(num)
print(f"Factorial of {num} is {fact}")

# Method 2 :
num=int(input("Enter the number : "))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(f"Factorial of {num} is {fact}")

# Method 3 : Recurison
 
def fact(num):
    if num==1:
        return 1
    else:
        return (num*fact(num-1))

num=int(input("Enter the number : "))

if num<=0:
    print("Enter a larger number than 0")
else:    
    print(f"Factorial of {num} is {fact(num)}")

