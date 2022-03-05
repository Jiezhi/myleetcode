#!/usr/bin/env python
"""
CREATED AT: 2022/3/5
Des:
https://leetcode.com/problems/longest-uncommon-subsequence-i/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def findLUSLength(self, a: str, b: str) -> int:
        """
        Runtime: 43 ms, faster than 44.35%
        Memory Usage: 13.9 MB, less than 77.25%
        1 <= a.length, b.length <= 100
        a and b consist of lower-case English letters.
        :param a:
        :param b:
        :return:
        """
        return -1 if a == b else max(len(a), len(b))


def test():
    assert Solution().findLUSLength("aba", "cdc") == 3


if __name__ == '__main__':
    test()
