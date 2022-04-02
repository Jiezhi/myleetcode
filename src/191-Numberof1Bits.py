#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/number-of-1-bits/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/565/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def hammingWeight2(self, n: int) -> int:
        """
        Runtime: 61 ms, faster than 13.99%
        Memory Usage: 13.8 MB, less than 53.47%

        :param n: The input must be a binary string of length 32.
        :return:
        """
        return n.bit_count()

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
    assert Solution().hammingWeight2(n=0x00000000000000000000000000001011) == 3


if __name__ == '__main__':
    test()
