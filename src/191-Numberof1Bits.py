#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/number-of-1-bits/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/565/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        601 / 601 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.2 MB
        :param n:
        :return:
        """
        return bin(n).count('1')


def test():
    assert Solution().hammingWeight(n=0x00000000000000000000000000001011) == 3


if __name__ == '__main__':
    test()
