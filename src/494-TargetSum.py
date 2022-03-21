#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:
https://leetcode.com/problems/target-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Runtime: 402 ms, faster than 59.94%
        Memory Usage: 36.1 MB, less than 18.65%

        1 <= nums.length <= 20
        0 <= nums[i] <= 1000
        0 <= sum(nums[i]) <= 1000
        -1000 <= target <= 1000
        """
        n = len(nums)

        @lru_cache(None)
        def dp(pos, num) -> int:
            ret = 0
            if pos == n - 1:
                if nums[pos] == num:
                    ret += 1
                if nums[pos] == -num:
                    ret += 1
                return ret

            return dp(pos + 1, num - nums[pos]) + dp(pos + 1, num + nums[pos])

        return dp(0, target)


def test():
    pass


if __name__ == '__main__':
    test()
