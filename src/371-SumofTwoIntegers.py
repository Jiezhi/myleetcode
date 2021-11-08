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
https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        It would be better to solve using Java.
        https://github.com/Jiezhi/LCOF-Java/blob/main/src/main/java/io.github.jiezhi.lcof/LCOF065.java
        
        -1000 <= a, b <= 1000
        :param a:
        :param b:
        :return:
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


def test():
    assert Solution().getSum(a=1, b=2) == 3
    assert Solution().getSum(a=2, b=3) == 5
    assert Solution().getSum(a=-1, b=1) == 0
    assert Solution().getSum(a=-1, b=0) == -1
    assert Solution().getSum(a=-12, b=-8) == -20


if __name__ == '__main__':
    test()
