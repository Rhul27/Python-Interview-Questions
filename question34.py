# Find Second Largest Number From List

num=[74,55,66,98,35,85,24,76]
# Method 1 :
num.sort()
print(f'Second Largest elements is {num[-2]}')

# Method 2 : (Wrong way don't do it a any interview)
num.remove(max(num))
print(f'Second Largest elements is {max(num)}')

# Method 3 :
largest=num[0]
second_largest=num[0]
for i in range(len(num)):
    if num[i]>largest:
        largest=num[i]

for i in range(len(num)):
    if num[i]>second_largest and num[i]!=largest:
        second_largest=num[i]

print(f'Second Largest elements is {second_largest}')

    

