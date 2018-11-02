"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
 @Author: Jiezhi 
 @Date: 2018-07-06 17:44:55 
 @Last Modified by:   Jiezhi 
 @Last Modified time: 2018-07-06 17:44:55 
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_substr = ''
        max_len = 0
        for c in s:
            if c not in max_substr:
                max_substr += c
            else:
                max_len = max(len(max_substr), max_len)
                max_substr = max_substr[max_substr.index(c) + 1:]
                max_substr += c
        max_len = max(len(max_substr), max_len)
        return max_len
        
if __name__ == '__main__':
    s = 'abcdcfge'
    print(Solution().lengthOfLongestSubstring(s))