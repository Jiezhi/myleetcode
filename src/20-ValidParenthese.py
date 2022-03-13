#!/usr/bin/env python
"""
https://leetcode.com/problems/valid-parentheses/description/
Created on 2018-11-08

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def isValid2(self, s: str) -> bool:
        """
        Solved at 2022/3/13
        Runtime: 49 ms, faster than 40.99%
        Memory Usage: 13.8 MB, less than 98.73%

        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.
        :param s:
        :return:
        """
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[c]:
                    return False
        return False if stack else True

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_list = ['(', '[', '{']
        right_list = [')', ']', '}']
        
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

    assert Solution().isValid2("")
    assert Solution().isValid2("()")
    assert Solution().isValid2("([])")
    assert Solution().isValid2("([{}])")
    assert Solution().isValid2("((") is False
    assert Solution().isValid2("([))") is False
    assert Solution().isValid2("([{]])") is False
    assert Solution().isValid2(")}") is False


if __name__ == '__main__':
    test()
