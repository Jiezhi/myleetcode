#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/4

Leetcode: https://leetcode.com/problems/rotate-array/

"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0 or k == len(nums):
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]


def test():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1]
    Solution().rotate(nums, 2)
    assert nums == [-1]

    nums = [1, 2, 3, 4, 5, 6]
    Solution().rotate(nums, 1)
    assert nums == [6, 1, 2, 3, 4, 5]


if __name__ == '__main__':
    test()
