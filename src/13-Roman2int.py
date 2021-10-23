#!/usr/bin/env python
"""
https://leetcode.com/problems/roman-to-integer/description/
Created on 2018-11-07

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""

romanDict = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return romanDict[s]
        ret = 0
        for i in range(len(s) - 1):
            n = romanDict[s[i]]
            if n >= romanDict[s[i + 1]]:
                ret += n
            else:
                ret -= n
        ret += romanDict[s[-1]]
        return ret


if __name__ == '__main__':
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("LVIII") == 58
