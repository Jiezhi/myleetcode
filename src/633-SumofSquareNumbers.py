#!/usr/bin/env python
"""
CREATED AT: 2021/8/25
Des:

https://leetcode.com/problems/sum-of-square-numbers/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3918/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import math
from functools import lru_cache


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        124 / 124 test cases passed.
        Status: Accepted
        Runtime: 304 ms
        Memory Usage: 14.2 MB
        :param c:
        :return:
        """
        i, j = 0, math.floor(math.sqrt(c))
        while i <= j:
            k = i ** 2 + j ** 2
            if k == c:
                return True
            if k < c:
                i += 1
            else:
                j -= 1
        return False


def test():
    assert not Solution().judgeSquareSum(c=88888888)
    assert Solution().judgeSquareSum(c=5)
    assert not Solution().judgeSquareSum(c=3)
    assert Solution().judgeSquareSum(c=4)
    assert Solution().judgeSquareSum(c=2)
    assert Solution().judgeSquareSum(c=1)


if __name__ == '__main__':
    test()
