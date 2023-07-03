# Check if strings are Anagrams or not

# what is Anagrams ?..
# Anagrams are words or phrases that can be formed by rearranging the letters of another
# word or phrase. In other words, anagrams are created by using all the original letters
# exactly once to form a new word or phrase with a different meaning. For example, the 
# word "listen" can be rearranged to form the word "silent," making "silent" an anagram
# of "listen." Anagrams can be a fun way to play with words and can often be found in 
# word games and puzzles.

str1=input("Enter the first string : ")
str2=input("Enter the second string : ")

if sorted(str1)==sorted(str2):
    print("These strings are anagrams")
else:
    print("These strings are not anagrams")