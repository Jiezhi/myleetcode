#!/usr/bin/env python3
"""
CREATED AT: 2022-11-27

URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1752-CheckIfArrayIsSortedAndRotated

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Runtime: 77 ms, faster than 14.32%
        Memory Usage: 13.9 MB, less than 14.05%
        1 <= nums.length <= 100
        1 <= nums[i] <= 100
        """
        rotated = False
        for i, num in enumerate(nums[1:], 1):
            if num < nums[i - 1]:
                if rotated or nums[0] < nums[-1]:
                    return False
                rotated = True
        return True


def test():
    assert Solution().check(nums=[3, 4, 5, 1, 2])
    assert not Solution().check(nums=[2, 1, 3, 4])
    assert Solution().check(nums=[1, 2, 3])


if __name__ == '__main__':
    test()
