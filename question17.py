# Factorial of the give number 

num=int(input("Enter the number : "))

# Method 1 : 
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(f"Factoiral is {fact}")


# Method 2 : Using Recurission
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
    
result=fact(num)
print(f"Factoiral of {num} is {result}")