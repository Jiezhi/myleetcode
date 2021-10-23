#!/usr/bin/env python
"""
CREATED AT: 2021/10/10
Des:

https://leetcode.com/problems/sum-of-two-integers/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: Bit Manipulation

Reference: https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        -1000 <= a, b <= 1000
        :param a:
        :param b:
        :return:
        """
        # while b != 0:
        #     a, b = a ^ b, (a & b) << 1
        #     print(a, b)
        # return a

        pass


def test():
    assert Solution().getSum(a=1, b=2) == 3
    assert Solution().getSum(a=2, b=3) == 5
    assert Solution().getSum(a=-1, b=1) == 0


if __name__ == '__main__':
    test()
