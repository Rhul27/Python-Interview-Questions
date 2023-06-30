# Iterate the list without using loop form start to end

lst=eval(input("Enter a list : "))
start=int(input("Enter start index : "))
end = int(input("Enter end index : "))
def iterate(lst,start,end):
    if start<0 or start>=end or end>=len(lst):
        return
    print(lst[start])
    iterate(lst,start+1,end)

iterate(lst,start,end)

