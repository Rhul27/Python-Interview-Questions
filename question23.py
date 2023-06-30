# Infosys Question

# You are given 'N' sticks each of negligible thickness and the 1thstick has lenght A[1].
# You have to form rectangles by choosing any four sticks.

# Find the maximum are of rectangle that is possible.

# Notes:-
# 1) Rectangle is a figure having opposite sides equal. 
# 2) A square is also a rectangle.

# Write a function rectangle which has following parameters.
# 1) Number of sticks (integer).
# 2) Integer arrry denoting length of sticks.

# Return value :- integer denoting maximum possible area.

# example1 :-
# Input : 5,[1,8,1,8,8]
# Output : 8
# Output description : We can create a rectangle of 8*1 and it has maximum area.

# example2 :-
# Input : 8,[4,2,3,2,3,4,5,1]
# Output : 12

# Algorithms :-
# 1) Remove those sticks which do not have pair.


# lst = eval(input("Enter a list"))
lst=[4,2,3,2,3,4,5,1]
lst1=[]
for i in lst:
    if lst.count(i)>1 and i not in lst1:
        lst1.append(i)
max=0
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i]*lst1[j]>max:
            max=lst1[i]*lst1[j]
print(max)

        
