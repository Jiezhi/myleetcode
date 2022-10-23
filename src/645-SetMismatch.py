#!/usr/bin/env python3
"""
CREATED AT: 2022-10-23

URL: https://leetcode.com/problems/set-mismatch/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 645-SetMismatch

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Runtime: 215 ms, faster than 90.47%
        Memory Usage: 15.4 MB, less than 74.26%

        2 <= nums.length <= 10^4
        1 <= nums[i] <= 10^4
        """
        repeat = None
        nums.append(0)
        for num in nums:
            if nums[abs(num)] < 0:
                repeat = abs(num)
            else:
                nums[abs(num)] *= -1
        for i, num in enumerate(nums):
            if num >= 0:
                return [repeat, i]


def test():
    assert Solution().findErrorNums(nums=[1, 2, 2, 4]) == [2, 3]
    assert Solution().findErrorNums(nums=[1, 1]) == [1, 2]
    assert Solution().findErrorNums(nums=[3, 2, 3, 4, 6, 5]) == [3, 1]


if __name__ == '__main__':
    test()
