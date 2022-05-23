#!/usr/bin/env python
"""
CREATED AT: 2022/5/23
Des:

https://leetcode.com/problems/ones-and-zeroes/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP

See: 

"""
from functools import lru_cache
from math import inf
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Runtime: 2028 ms, faster than 95.84%
        Memory Usage: 307.3 MB, less than 5.05%
        :param strs:
        :param m:
        :param n:
        1 <= strs.length <= 600
        1 <= strs[i].length <= 100
        strs[i] consists only of digits '0' and '1'.
        1 <= m, n <= 100
        :return:
        """
        arr = []

        for s in strs:
            ones = 0
            zeros = 0
            for c in s:
                if c == '1':
                    ones += 1
                else:
                    zeros += 1
            if zeros > m or ones > n:
                continue
            arr.append((zeros, ones))

        @lru_cache(None)
        def dp(pos, m, n) -> int:
            if m < 0 or n < 0:
                return -inf
            if pos >= len(arr):
                return 0

            return max(dp(pos + 1, m, n), 1 + dp(pos + 1, m - arr[pos][0], n - arr[pos][1]))

        ret = dp(0, m, n)
        return ret if ret > 0 else 0


def test():
    assert Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4


if __name__ == '__main__':
    test()
