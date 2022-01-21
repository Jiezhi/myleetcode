#!/usr/bin/env python
"""
CREATED AT: 2022/1/21
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

Time Spent:  min
"""
from functools import lru_cache
from typing import List


class Solution:
    def minDifficulty2(self, jobDifficulty: List[int], d: int) -> int:
        """
        CREATED AT: 2022/1/21
        34 / 34 test cases passed.
        Status: Accepted
        Runtime: 8216 ms
        Memory Usage: 17.1 MB
        1 <= jobDifficulty.length <= 300
        0 <= jobDifficulty[i] <= 1000
        1 <= d <= 10
        :param jobDifficulty:
        :param d:
        :return:
        """
        # bottom to top
        # TODO

        # n = len(jobDifficulty)
        # dp = [[0 for _ in range(d + 1)] for _ in range(n + 1)]
        # for i in range(n - 1, -1, -1):
        #     for k in range(d, -1, -1):
        #         dp[i][k] = min(max(jobDifficulty[i:i + x]) + dp[i + x][k] for x in range(1, n + 1))
        #
        # return dp[0][0]
        return -1

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        CREATED AT: 2022/1/21
        34 / 34 test cases passed.
        Status: Accepted
        Runtime: 8216 ms
        Memory Usage: 17.1 MB
        1 <= jobDifficulty.length <= 300
        0 <= jobDifficulty[i] <= 1000
        1 <= d <= 10
        :param jobDifficulty:
        :param d:
        :return:
        """
        # top to bottom
        max_value = 2 ** 31
        n = len(jobDifficulty)

        @lru_cache(None)
        def dp(i, d) -> int:
            if i >= n and d == 0:
                return 0
            elif d == 0:
                return max_value
            if n - i < d:
                return max_value
            return min(max(jobDifficulty[i:i + x]) + dp(i + x, d - 1) for x in range(1, n + 1))

        ret = dp(0, d)
        return ret if ret < max_value else -1


def test():
    assert Solution().minDifficulty(
        jobDifficulty=[
            186, 398, 479, 206, 885, 423, 805, 112, 925, 656, 16, 932, 740, 292, 671, 360
        ], d=4) == 1803
    assert Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=3) == 9
    assert Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2) == 7
    assert Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=1) == 6
    assert Solution().minDifficulty(jobDifficulty=[9, 9, 9], d=4) == -1
    assert Solution().minDifficulty(jobDifficulty=[1, 1, 1], d=3) == 3


if __name__ == '__main__':
    test()
