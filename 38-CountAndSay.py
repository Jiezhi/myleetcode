#!/usr/bin/env python
"""
https://leetcode.com/problems/count-and-say/description/
Created on 2018-11-13

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n - 1):
            tmp = s[0]
            count = 0
            tmp_s = ""
            for c in s:
                if c == tmp:
                    count += 1
                else:
                    tmp_s += '{}{}'.format(count, tmp)
                    tmp = c
                    count = 1
            tmp_s += '{}{}'.format(count, tmp)
            s = tmp_s
        return s


def test():
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
