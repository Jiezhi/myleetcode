#!/usr/bin/env python
"""
CREATED AT: 2021/11/18
Des:

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List

from src import tool


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Runtime: 376 ms, faster than 49.95%
        Memory Usage: 21.9 MB, less than 73.73%
        n == nums.length
        1 <= n <= 10^5
        1 <= nums[i] <= n
        :param nums:
        :return:
        """
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [x + 1 for x in range(len(nums)) if nums[x] > 0]


def test():
    assert tool.equal_list_value(Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
    assert Solution().findDisappearedNumbers(nums=[1, 1]) == [2]


if __name__ == '__main__':
    test()
