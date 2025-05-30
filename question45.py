# Maximum Number of Words You Can Type

# xample 1:

# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.
# Example 2:

# Input: text = "leet code", brokenLetters = "lt"
# Output: 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
# Example 3:

# Input: text = "leet code", brokenLetters = "e"
# Output: 0
# Explanation: We cannot type either word because the 'e' key is broken.
 
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(1 for word in text.split() if not any(c in broken for c in word))

# class Solution:
#     def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
#         words = text.split()
#         count = len(words)
#         for word in words:
#             for letter in brokenLetters:
#                 if letter in word:
#                     count -= 1
#                     break
#         return count

 