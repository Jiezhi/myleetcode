#!/usr/bin/env python
"""
CREATED AT: 2021/12/3
Des:

https://leetcode.com/problems/maximum-product-subarray/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP

See: 
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Runtime: 60 ms, faster than 43.10%
        Memory Usage: 14.1 MB, less than 95.16%
        1 <= nums.length <= 2 * 10^4
        -10 <= nums[i] <= 10
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        :param nums:
        :return:
        """
        pre_dp = [nums[0], nums[0]]
        ret = nums[0]
        for num in nums[1:]:
            cur_dp = [max(num, pre_dp[0] * num, pre_dp[1] * num), min(num, pre_dp[0] * num, pre_dp[1] * num)]
            pre_dp[0] = cur_dp[0]
            pre_dp[1] = cur_dp[1]
            ret = max(ret, cur_dp[0])
        return ret


def test():
    assert Solution().maxProduct(nums=[2, 3, -2, 4]) == 6
    assert Solution().maxProduct(nums=[2, 3, -2, 4, -1]) == 48
    assert Solution().maxProduct(nums=[-2, 0, -1]) == 0
    assert Solution().maxProduct(nums=[-2]) == -2
    assert Solution().maxProduct(nums=[-2, 1]) == 1
    assert Solution().maxProduct(nums=[-2, 1, -1]) == 2


if __name__ == '__main__':
    test()
