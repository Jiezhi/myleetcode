#!/usr/bin/env python
"""
https://leetcode.com/problems/length-of-last-word/description/
Created on 2018-11-14

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])


def test():
    assert Solution().lengthOfLastWord('Hello World') == 5
    assert Solution().lengthOfLastWord('') == 0
    assert Solution().lengthOfLastWord('a ') == 1
