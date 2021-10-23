#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/12

Leetcode: https://leetcode.com/problems/move-zeroes/

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums) - 1
        i = 0
        while i < l:
            if nums[i] == 0:
                l -= 1
                nums[i:] = nums[i + 1:] + [0]
            else:
                i += 1

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if zeros > 0:
                nums[i - zeros] = nums[i]
            if nums[i] == 0:
                zeros += 1
        if zeros > 0:
            nums[-zeros:] = [0] * zeros


def test():
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 0, 1]
    Solution().moveZeroes(nums)
    assert nums == [1, 0, 0]

    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes2(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 0, 1]
    Solution().moveZeroes2(nums)
    assert nums == [1, 0, 0]

    nums = [1]
    Solution().moveZeroes2(nums)
    assert nums == [1]


if __name__ == '__main__':
    test()
