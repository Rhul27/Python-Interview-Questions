# Longest Common Prefix

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            char = strs[0][i]  
            for s in strs[1:]: 
                if s[i] != char:
                    return strs[0][:i]
        return strs[0][:min_len]
