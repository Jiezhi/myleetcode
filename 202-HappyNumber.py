#!/usr/bin/env python
"""
CREATED AT: 2021/9/9
Des:

https://leetcode.com/problems/happy-number
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        402 / 402 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14 MB
        :param n:
        :return:
        """
        if n == 1:
            return True

        def replace(num) -> int:
            i, j = divmod(num, 10)
            ret = j * j
            while i >= 10:
                i, j = divmod(i, 10)
                ret += j * j
            ret += i * i
            return ret

        circle = []

        while n not in circle:
            circle.append(n)
            n = replace(n)
            if n == 1:
                return True
        return False


def test():
    assert Solution().isHappy(n=19)
    assert Solution().isHappy(n=1)
    assert not Solution().isHappy(n=2)


if __name__ == '__main__':
    test()
