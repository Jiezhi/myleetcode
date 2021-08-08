#!/usr/bin/env python
"""
CREATED AT: 2021/8/8
Des:
https://leetcode.com/contest/weekly-contest-253/problems/check-if-string-is-a-prefix-of-array/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ret = ''
        for word in words:
            ret += word
            if s == ret:
                return True
            elif len(ret) >= len(s):
                return False
        return False


def test():
    assert Solution().isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"])
    assert not Solution().isPrefixString(s="iloveleetcode", words=["apples", "i", "love", "leetcode"])


if __name__ == '__main__':
    test()
