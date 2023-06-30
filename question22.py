# To find a pair a higest product from a list

# input=[2,5,6,4,9,7,6,3,4,6]
# output=[7,9]

arr=eval(input("Enter the list : "))
arr_len=len(arr)
if arr_len<2:
    print("No such pair exits")
a=arr[0]
b=arr[1]
for i in range(0,arr_len):
    for j in range(i+1,arr_len):
        if (arr[i]*arr[j])>(a*b):
            a=arr[i]
            b=arr[j]
print(f"Maxium Product is {a} and {b}")
