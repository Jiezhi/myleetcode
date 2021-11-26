#!/usr/bin/env python
"""
https://leetcode.com/problems/search-insert-position/description/
Created on 2018-11-13

@author: 'Jiezhi.G@gmail.com'

解题思路：乍一看，题目很简单，直接遍历一下基本就可以得到答案了：
```
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums) + 1
```
但是题目中提到是已经排好序的数组了，所以主要考察的是二分查找
Reference: 
"""
from typing import List

from tool import print_results


class Solution:
    @print_results
    def searchInsert2(self, nums: List[int], target: int) -> int:
        """
        20210824 do it again
        Runtime: 63 ms, faster than 22.19%
        Memory Usage: 15 MB, less than 56.94%
        :param nums:
        :param target:
        :return:
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        # now high = low - 1
        if high >= 0 and nums[high] > target:
            return high
        return low

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # method 1
        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start


def binarySearch(start, end, nums, target):
    if nums[start] >= target:
        return start
    if nums[end] == target:
        return end
    if nums[end] < target:
        return end + 1
    mid = start + (end - start) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearch(start, mid - 1, nums, target)
    elif nums[mid] < target:
        return binarySearch(mid + 1, end, nums, target)


def test():
    assert Solution().searchInsert([1], 0) == 0
    assert Solution().searchInsert([1], 2) == 1
    assert Solution().searchInsert([1, 3], 3) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert2([1], 0) == 0
    assert Solution().searchInsert2([1], 2) == 1
    assert Solution().searchInsert2([1, 3], 3) == 1
    assert Solution().searchInsert2([1, 3, 4, 5, 6], 3) == 1
    assert Solution().searchInsert2([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert2([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert2([1, 3, 5, 6], 7) == 4


if __name__ == '__main__':
    test()
