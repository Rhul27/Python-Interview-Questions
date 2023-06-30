# Read a text file and give number of lines, words and characters present in the text file

f=open('hello.txt',mode="r")
num_of_line=0
num_of_words=0
num_of_characters=0

for line in f:
    num_of_line+=1
    line=line.strip("\n")
    num_of_characters+=len(line)
    lst=line.split()
    num_of_words+=len(lst)

print("Number of lines",num_of_line)
print("Number of Words",num_of_words)
print("Number of Characters",num_of_characters)