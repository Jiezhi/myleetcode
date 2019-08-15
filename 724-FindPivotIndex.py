#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-08-15

Leetcode: 

"""


class Solution:
    def pivotIndex(self, nums: list) -> int:
        if not nums:
            return -1
        # Or just sum(nums)
        sum = 0
        for i in nums:
            sum += i
        left = 0
        right = sum
        if sum - nums[0] == 0:
            return 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left == right - nums[i + 1]:
                return i + 1
        return -1


def test():
    assert Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert Solution().pivotIndex([1, 2, 3]) == -1
    assert Solution().pivotIndex([-1, -1, -1, 0, 1, 1]) == 0


if __name__ == '__main__':
    test()
