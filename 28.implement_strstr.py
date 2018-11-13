#!/usr/bin/env python
"""
https://leetcode.com/problems/implement-strstr/description/
Created on 2018-11-13

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or haystack == needle:
            return 0
        len_n = len(needle)
        for i in range(len(haystack) - len_n + 1):
            if haystack[i:i + len_n] == needle:
                return i
        return -1


if __name__ == '__main__':
    assert Solution().strStr("test", "") == 0
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("hello", "k") == -1
    assert Solution().strStr("hello", "hello") == 0
    assert Solution().strStr("mississippi", "pi") == 9
    pass
