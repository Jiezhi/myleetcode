#!/usr/bin/env python3
"""
CREATED AT: 2022-12-11

URL: https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1827-MinimumOperationsToMakeTheArrayIncreasing

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 5000
        1 <= nums[i] <= 10^4
        """
        ret, pre = 0, nums[0] - 1
        for num in nums:
            if num <= pre:
                pre += 1
                ret += pre - num
            else:
                pre = num
        return ret


def test():
    assert Solution().minOperations(nums=[1, 1, 1]) == 3
    assert Solution().minOperations(nums=[1, 5, 2, 4, 1]) == 14
    assert Solution().minOperations(nums=[8]) == 0


if __name__ == '__main__':
    test()
