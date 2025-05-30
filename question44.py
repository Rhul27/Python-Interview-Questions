# Check if All Characters Have Equal Number of Occurrences

# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return len(set(count.values())) == 1
    

s = "abacbc"
solution = Solution()
print(solution.areOccurrencesEqual(s))
