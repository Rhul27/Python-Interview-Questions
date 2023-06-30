# Question : lower case the string without using string method

# Uppercase Letters (A-Z):
# ---------------------------
# Minimum ASCII value: 65 value of "A"
# Maximum ASCII value: 90 value of "Z"

# Lowercase Letters (a-z):
# ----------------------------
# Minimum ASCII value: 97 value of "a"
# Maximum ASCII value: 122 value of "z"

# Difference between UpperLetters and lowerLetters is 32


str1=input("Enter a string : ")
lower=""
for ch in str1:
    asci=ord(ch)
    if asci>64 and asci<91:
        lower=lower+chr(asci+32)
    else:
        lower=lower+chr(asci)
print("Lower Case : ",lower)
