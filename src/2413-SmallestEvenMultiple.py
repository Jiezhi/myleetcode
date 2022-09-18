#!/usr/bin/env python3
"""
CREATED AT: 2022-09-18

URL: https://leetcode.com/problems/smallest-even-multiple/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2413-SmallestEvenMultiple

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
        1 <= n <= 150
        """
        return n if (n & 1 == 0) else n * 2


def test():
    assert Solution().smallestEvenMultiple(n=5) == 10
    assert Solution().smallestEvenMultiple(n=6) == 6


if __name__ == '__main__':
    test()
