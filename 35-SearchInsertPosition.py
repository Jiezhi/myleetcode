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


class Solution:
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
        # method 2
        # return binarySearch(0, len(nums) - 1, nums, target)


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
    # print(Solution().searchInsert([1, 3, 5, 6], 2))
    # print(binarySearch(0, 3, [1, 3, 5, 6], 2))
    assert Solution().searchInsert([1], 0) == 0
    assert Solution().searchInsert([1, 3], 3) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
