#!/usr/bin/env python3
"""
CREATED AT: 2022-10-07

URL: https://leetcode.com/problems/maximum-ascending-subarray-sum/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1800-MaximumAscendingSubarraySum

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Runtime: 45 ms, faster than 79.61%
        Memory Usage: 13.9 MB, less than 13.69%

        1 <= nums.length <= 100
        1 <= nums[i] <= 100
        """
        ret, cur, pre = 0, 0, 0
        for num in nums:
            if num > pre:
                cur += num
            else:
                cur = num
            pre = num
            ret = max(ret, cur)
        return ret


def test():
    assert Solution().maxAscendingSum(nums=[10, 20, 30, 5, 10, 50]) == 65
    assert Solution().maxAscendingSum(nums=[10, 20, 30, 40, 50]) == 150
    assert Solution().maxAscendingSum(nums=[12, 17, 15, 13, 10, 11, 12]) == 33


if __name__ == '__main__':
    test()
