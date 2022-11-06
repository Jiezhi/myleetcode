#!/usr/bin/env python3
"""
CREATED AT: 2022-11-06

URL: https://leetcode.com/problems/apply-operations-to-an-array/
https://leetcode.com/contest/weekly-contest-318/problems/apply-operations-to-an-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2460-ApplyOperationsToAnArray

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        2 <= nums.length <= 2000
        0 <= nums[i] <= 1000
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        ret = [num for num in nums if num != 0]
        return ret + [0] * (len(nums) - len(ret))


def test():
    assert Solution().applyOperations(nums=[1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]
    assert Solution().applyOperations(nums=[0, 1]) == [1, 0]


if __name__ == '__main__':
    test()
