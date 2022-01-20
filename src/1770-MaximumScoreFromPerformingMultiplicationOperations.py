#!/usr/bin/env python
"""
CREATED AT: 2022/1/20
Des:

https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
https://leetcode.com/explore/featured/card/dynamic-programming/631/strategy-for-solving-dp-problems/4146/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: https://leetcode.com/explore/featured/card/dynamic-programming/631/strategy-for-solving-dp-problems/4100/

Time Spent:  min
"""
from typing import List


class Solution:
    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        """
        CREATED AT: 2022/1/20
        62 / 62 test cases passed.
        Status: Accepted
        Runtime: 7939 ms
        Memory Usage: 41.4 MB

        n == nums.length
        m == multipliers.length
        1 <= m <= 10^3
        m <= n <= 10^5
        -1000 <= nums[i], multipliers[i] <= 1000
        :param nums:
        :param multipliers:
        :return:
        """
        dp = [[0] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)]
        for i in range(len(multipliers) - 1, -1, -1):
            for left in range(i, -1, -1):
                right = len(nums) - 1 - (i - left)
                dp[i][left] = max(multipliers[i] * nums[left] + dp[i + 1][left + 1],
                                  multipliers[i] * nums[right] + dp[i + 1][left])
        return dp[0][0]

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        CREATED AT: 2022/1/20
        Memory Limit Exceeded for    @lru_cache(None)
        LTE for @lru_cache(2000)
        n == nums.length
        m == multipliers.length
        1 <= m <= 10^3
        m <= n <= 10^5
        -1000 <= nums[i], multipliers[i] <= 1000
        :param nums:
        :param multipliers:
        :return:
        """

        # Top to bottom
        dp_memo = [[0 for _ in range(len(multipliers))] for _ in range(len(multipliers))]

        def dp(i, left):
            if i >= len(multipliers):
                return 0
            if dp_memo[i][left]:
                return dp_memo[i][left]

            right = len(nums) - i + left - 1
            ret = max(multipliers[i] * nums[left] + dp(i + 1, left + 1),
                      multipliers[i] * nums[right] + dp(i + 1, left))
            dp_memo[i][left] = ret
            return ret

        return dp(0, 0)


def test():
    assert Solution().maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]) == 14
    assert Solution().maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]) == 102


if __name__ == '__main__':
    test()
