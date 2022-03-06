#!/usr/bin/env python
"""
CREATED AT: 2022/3/6
Des:

https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        """
        2 <= nums.length <= 1000
        1 <= nums[i] <= 1000
        The test cases will be generated such that the answer is unique.
        """
        cnts = collections.defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnts[nums[i + 1]] += 1
        ret = 0
        max_cnt = 0
        for key, value in cnts.items():
            if value > max_cnt:
                max_cnt = value
                ret = key
        return ret


def test():
    assert Solution().mostFrequent(nums=[1, 100, 200, 1, 100], key=1) == 100
    assert Solution().mostFrequent(nums=[2, 2, 2, 2, 3], key=2) == 2


if __name__ == '__main__':
    test()
