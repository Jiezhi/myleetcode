#!/usr/bin/env python
"""
CREATED AT: 2021/10/14
Des:
https://leetcode.com/problems/combination-sum-iv/
https://leetcode.com/study-plan/dynamic-programming/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

TAG: DP
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Runtime: 53 ms, faster than 28.17%
        Memory Usage: 14.1 MB, less than 88.37%
        1 <= nums.length <= 200
        1 <= nums[i] <= 1000
        All the elements of nums are unique.
        1 <= target <= 1000
        :param nums:
        :param target:
        :return:
        """
        dp = [0 for _ in range(target + 1)]
        nums = sorted(nums)
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - num]
        return dp[-1]


def test():
    assert Solution().combinationSum4(nums=[1], target=1) == 1
    assert Solution().combinationSum4(nums=[1, 2, 3], target=4) == 7
    assert Solution().combinationSum4(nums=[9], target=3) == 0
    assert Solution().combinationSum4(nums=[1], target=1000) == 1


if __name__ == '__main__':
    test()
