#!/usr/bin/env python
"""
CREATED AT: 2022/3/27
Des:
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
from functools import lru_cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """
        Runtime: 6770 ms, faster than 33.33%
        Memory Usage: 140.6 MB, less than 11.11%

        n == piles.length
        1 <= n <= 1000
        1 <= piles[i][j] <= 10^5
        1 <= k <= sum(piles[i].length) <= 2000
        """

        @lru_cache(None)
        def dp(pos, k) -> int:
            if k == 0 or pos == len(piles):
                return 0
            ret = dp(pos + 1, k)
            taken = 0
            for i in range(min(k, len(piles[pos]))):
                taken += piles[pos][i]
                ret = max(ret, taken + dp(pos + 1, k - i - 1))
            return ret

        return dp(0, k)


def test():
    assert Solution().maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2) == 101
    assert Solution().maxValueOfCoins(piles=[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]],
                                      k=7) == 706


if __name__ == '__main__':
    test()
