#!/usr/bin/env python
"""
CREATED AT: 2022/3/28
Des:
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 33

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Runtime: 73 ms, faster than 54.24%
        Memory Usage: 14.4 MB, less than 95.32%

        1 <= nums.length <= 5000
        -10^4 <= nums[i] <= 10^4
        nums is guaranteed to be rotated at some pivot.
        -10^4 <= target <= 10^4
        """
        if not nums:
            return False
        mid = len(nums) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > nums[0]:
            if target > nums[mid] or target < nums[0]:
                return self.search(nums[mid + 1:], target)
            else:
                return self.search(nums[:mid], target)
        elif nums[mid] < nums[-1]:
            if target > nums[-1] or target < nums[mid]:
                return self.search(nums[:mid], target)

            else:
                return self.search(nums[mid + 1:], target)
        else:
            return self.search(nums[:mid], target) or self.search(nums[mid + 1:], target)


def test():
    assert Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0)
    assert not Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=3)


if __name__ == '__main__':
    test()
