#!/usr/bin/env python
"""
CREATED AT: 2021/10/12
Des:
https://leetcode.com/problems/guess-number-higher-or-lower/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""

actual = -1


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    if num == actual:
        return 0
    if num < actual:
        return 1
    if num > actual:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Runtime: 20 ms, faster than 99.12%
        Memory Usage: 14 MB, less than 97.81%
        :param n:
        :return:
        """
        l, h = 1, n
        while True:
            mid = l + (h - l) // 2
            ret = guess(mid)
            if ret == 0:
                return mid
            if ret < 0:
                h = mid - 1
            else:
                l = mid + 1


def test():
    global actual
    actual = 6
    assert Solution().guessNumber(n=10) == actual
    actual = 1
    assert Solution().guessNumber(n=2) == actual
    actual = 2
    assert Solution().guessNumber(n=2) == actual


if __name__ == '__main__':
    test()
