# Infosys Coding Question

# Given an array of integers 'nums' and an integer 'target'.
# return indices of two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# 
# You can return answer in any order.
# 
# Input :- nums = [2,7,11,15]
#          target = 9
# Output :- [0,1]


# Input :- nums = [3,2,4]
#          target = 6
# Output :- [1,2]
# 


# Input :- nums = [3,3]
#          target = 6
# Output :- [0,1]


nums=eval(input("Enter a list : "))
target=int(input("Enter a target : "))
output=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target and len(output)==0:
            output.append(i)
            output.append(j)
print(output)
