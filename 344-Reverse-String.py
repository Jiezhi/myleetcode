#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-07-12

Leetcode: https://leetcode.com/problems/reverse-string/

"""
import math


class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(math.ceil(l / 2)):
            s[i], s[l - i - 1] = s[l - i - 1], s[i]


def test():
    s = []
    Solution().reverseString(s)
    assert s == []
    s = ['H']
    Solution().reverseString(s)
    assert s == ['H']
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    assert s == ['o', 'l', 'l', 'e', 'h']
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
    s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",",
         " ", "a", " ", "c", "a", "n", "a", "l", ":", " ", "P", "a", "n", "a", "m", "a"]
    Solution().reverseString(s)
    assert s == ["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ",
                 "a", " ", ",", "n", "a", "l", "p", " ", "a", " ", ",", "n", "a", "m", " ", "A"]


if __name__ == '__main__':
    test()
