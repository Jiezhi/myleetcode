#!/usr/bin/env python
"""
https://leetcode.com/problems/regular-expression-matching/
Created on 2018-12-07

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        patters = p.split('*')
        last_p = patters[-1]
        if last_p:
            if len(last_p) > len(s):
                return False
            last_s = s[-len(last_p):]
            for i in range(len(last_s)):
                if last_p[i] != '.' and last_p[i] != last_s[i]:
                    return False
            s = s[:-len(last_p)]
            p = p[:-len(last_p)]
        i = 0
        j = 0
        last_pc = ''
        while i < len(s) and j < len(p):
            sc = s[i]
            pc = p[j]
            if pc == '*':
                if last_pc == '.' or sc == last_pc:
                    i += 1
                else:
                    j += 1
            elif pc == '.' or pc == sc:
                i += 1
                j += 1
                last_pc = pc
            elif j < len(p) - 1 and p[j + 1] == '*':
                # pc != sc
                j += 2
                last_pc = ''
            else:
                return False

        if i < len(s) or j > len(p):
            return False
        for i in range(j, len(p)):
            if p[i] != '*' and i < len(p) - 1 and p[i + 1] != '*':
                # and p[i] != last_pc:
                return False
        return True


def test():
    return
    assert not Solution().isMatch('aa', 'a')
    assert Solution().isMatch('aa', 'a*')
    assert Solution().isMatch('ab', '.*')
    assert Solution().isMatch('aaa', '.*')
    assert Solution().isMatch('aab', 'c*a*b')
    assert not Solution().isMatch("mississippi", 'mis*is*p*.')
    assert Solution().isMatch("mississippi", "mis*is*ip*.")
    assert not Solution().isMatch("aaba", "ab*a*c*a")
    assert Solution().isMatch("aaa", "a*a")
    assert Solution().isMatch("aaa", "a*aa")
    assert not Solution().isMatch("aaa", "a*aaaa")
    assert not Solution().isMatch("aaa", "aaaa")
    assert not Solution().isMatch("abcd", "d*")
    assert Solution().isMatch("aaa", "ab*ac*a")
    assert Solution().isMatch("aaa", "ab*a*c*a")
    assert not Solution().isMatch("a", ".*..a*")
    assert Solution().isMatch("ab", ".*..c*")
