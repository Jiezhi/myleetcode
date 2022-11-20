#!/usr/bin/env python3
"""
CREATED AT: 2022-11-20

URL: https://leetcode.com/problems/number-of-unequal-triplets-in-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2475-NumberOfUnequalTripletsInArray

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        """
        3 <= nums.length <= 100
        1 <= nums[i] <= 1000
        """
        n = len(nums)
        ret = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        ret += 1
        return ret


def test():
    assert Solution().unequalTriplets(nums=[4, 4, 2, 4, 3]) == 3
    assert Solution().unequalTriplets(nums=[1, 1, 1, 1, 1]) == 0


if __name__ == '__main__':
    test()
