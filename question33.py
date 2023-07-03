# Input : 
# ['1234python668','678java899','4566hadoop9123']
# Output : 
# int = [1234668,678899,45669123]
# str = ['python','java','hadoop']

p = ['1234python668','678java899','4566hadoop9123']
int_lst=[]
char_lst=[]
for i in p:
    int_var=''
    char_var=''
    for j in i:
        if j.isdigit():
            int_var=int_var+j
        else:
            char_var=char_var+j
    int_lst.append(int(int_var))
    char_lst.append(char_var)
print(int_lst)
print(char_lst)
        