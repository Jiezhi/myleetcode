#!/usr/bin/env python3
"""
CREATED AT: 2022-10-18

URL: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 902-NumbersAtMostNGivenDigitSet

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """
        Runtime: 66 ms, faster than 12.12%
        Memory Usage: 13.9 MB, less than 84.85%

        1 <= digits.length <= 9
        digits[i].length == 1
        digits[i] is a digit from '1' to '9'.
        All the values in digits are unique.
        digits is sorted in non-decreasing order.
        1 <= n <= 10^9
        """
        ret = 0
        digit_len = len(digits)
        n = list(str(n))
        num_len = len(n)

        # all combinations of length smaller than n
        tmp = digit_len
        for i in range(1, num_len):
            ret += tmp
            tmp *= digit_len

        def dfs(i) -> int:
            if i >= num_len:
                return 1
            equal = False
            smaller = 0
            for d in digits:
                if d < n[i]:
                    smaller += 1
                elif d == n[i]:
                    equal = True
                else:
                    break
            r = 0
            # two situations
            # 1. count digits smaller than current i'th n digit
            if smaller:
                r += smaller * digit_len ** (num_len - i - 1)
            # 2. calculate the valid counts afterwards
            if equal:
                r += dfs(i + 1)
            return r

        # calculate the valid combinations of same length
        ret += dfs(0)
        return ret


def test():
    assert Solution().atMostNGivenDigitSet(digits=["1", "3", "5", "7"], n=100) == 20
    assert Solution().atMostNGivenDigitSet(digits=["1", "4", "9"], n=1000000000) == 29523
    assert Solution().atMostNGivenDigitSet(digits=["7"], n=8) == 1


if __name__ == '__main__':
    test()
