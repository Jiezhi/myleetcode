#!/usr/bin/env python
"""
https://leetcode.com/problems/longest-common-prefix/description/
Created on 2018-11-07

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        str1 = strs[0]
        longest = ""
        for c in str1:
            longest += c
            for s in strs[1:]:
                if not s.startswith(longest):
                    return longest[:-1]
        return longest


def test():
    assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix(["dog", "dog", "dog"]) == "dog"
