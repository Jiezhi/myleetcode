#!/usr/bin/env python
"""
https://leetcode.com/problems/regular-expression-matching/
Created on 2018-12-07

@author: 'Jiezhi.G@gmail.com'
很尴尬，没注意审题，把*号当通配符来用了，而题目中意思是指*号前面的字符出现0次或多次。
然而，目前看来按审错题的思路来看，功能已经实现了，删掉了还是有点可惜的，所以就把代码保留了，也用来警醒自己『注意审题』!

Reference: 
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = p.split('*')
        l = len(pattern)
        if l == 1:
            # there's no '*' in patter string
            return isSubMatch(s, p)
        if len(''.join(pattern)) > len(s):
            return False
        if not isSubMatch(pp=pattern[0], ss=s[:len(pattern[0])]):
            # are head and tail str match?
            return False
        s = s[len(pattern[0]):]
        for m_pattern in pattern[1:]:
            if m_pattern == '':
                continue
            pos = s.find(m_pattern[0])
            if pos < 0 or not isSubMatch(s[pos:pos + len(m_pattern)], m_pattern):
                return False
            s = s[pos + len(m_pattern):]
        return True


def isSubMatch(ss, pp):
    if len(pp) == 0:
        return True
    if len(ss) != len(pp):
        return False
    for i in range(len(ss)):
        if pp[i] != '.' and pp[i] != ss[i]:
            return False
    return True


def test():
    assert isSubMatch('', '')
    assert isSubMatch('aa', '')
    assert isSubMatch('aa', 'aa')
    assert not isSubMatch('aa', 'bb')
    assert isSubMatch('aa', 'a.')
    assert isSubMatch('aa', 'aa')
    assert not Solution().isMatch('aa', 'a')
    assert Solution().isMatch('aa', 'a*')
    assert Solution().isMatch('ab', '.*')
    assert Solution().isMatch('aab', 'a*a*b')
    assert not Solution().isMatch("mississippi", 'mis*is*p*.')
