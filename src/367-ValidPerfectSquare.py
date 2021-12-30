#!/usr/bin/env python
"""
CREATED AT: 2021/12/30
Des:

https://leetcode.com/problems/valid-perfect-square/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: BS

See: 

Time Spent: 1 min
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        70 / 70 test cases passed.
        Status: Accepted
        Runtime: 39 ms
        Memory Usage: 14.3 MB
        1 <= num <= 2^31 - 1
        :param num:
        :return:
        """
        if num == 1:
            return True
        low, high = 0, num // 2
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1
        return False


def test():
    assert Solution().isPerfectSquare(num=1)
    assert not Solution().isPerfectSquare(num=2)
    assert Solution().isPerfectSquare(num=16)
    assert not Solution().isPerfectSquare(num=14)


if __name__ == '__main__':
    test()
