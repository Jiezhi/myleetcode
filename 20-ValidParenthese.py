#!/usr/bin/env python
"""
https://leetcode.com/problems/valid-parentheses/description/
Created on 2018-11-08

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
left_list = ['(', '[', '{']
right_list = [')', ']', '}']


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 != 0 or s[0] not in left_list or s[-1] not in right_list:
            return False
        l = list()
        for c in s:
            if c in left_list:
                l.append(c)
            else:
                if not l:
                    return False
                pop_c = l.pop()
                if left_list.index(pop_c) != right_list.index(c):
                    return False
        if l:
            return False
        return True


def test():
    assert Solution().isValid("")
    assert Solution().isValid("()")
    assert Solution().isValid("([])")
    assert Solution().isValid("([{}])")
    assert Solution().isValid("((") is False
    assert Solution().isValid("([))") is False
    assert Solution().isValid("([{]])") is False
    assert Solution().isValid(")}") is False
