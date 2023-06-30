# Infosys Question

# An e-commerce site has a series of advertisements to display.Links to the ads are 
# stores in a data structure and they are displayed or not is based on the value at 
# bit position in a number. The sequence of ads being displayed at the time can be
# represented as a binary value. Where 1 eans the ad is displayed and 0 means ad is
# not displayed. The ads should rotate. So, when the next page loads, ads that are 
# displayed now are hidden and vice versa

# sample input:
# 50
# sample output:
# 13

def changeads(num):
    b=bin(num)
    b=b[2:]
    bits=""
    for bit in b:
        if bit=="1":
            bits+="0"
        else:
            bits+="1"
    sum1=0
    for i in range(len(bits)):
        sum1=sum1+int(bits[i])*(2**(len(bits)-(i+1)))
    return sum1

print(changeads(20))
