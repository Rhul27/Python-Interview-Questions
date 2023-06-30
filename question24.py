# Infosys Question

# You are given a string s of length n and an array of strings t containing
# m strings each of lenght n-1.
# you need to remove one character from s such that s become equals to any of m strings.

# Find the total number of strings from the m given strings which can be 
# obtained by removing one character from s 

# Input :-
# lenght of string s (n) :- 5
# Enter string (s) :- 'abcde'

# number of strings in t (m) :- 4
# enter strings (t) :- ['abcd','abcc','cddd','acde']

# output :- 2

def func(n,s,m,t):
    count=0
    lst=[]
    for i in m:
        lst.append(i)
    for i in range(n):
        a=lst.pop(i)
        for word in t:
            if "".join(lst)==word:
                count+=1
        lst.insert(i,a)
    return count

print(func(5,4,'abcde',['abcd','abcc','cddd','acde']))