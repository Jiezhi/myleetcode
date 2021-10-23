#!/usr/bin/env python
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Created on 2018-11-11

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        l = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[l]:
                l += 1
                nums[l] = nums[i]
        return l + 1


def printRet(nums, l):
    for i in range(l):
        print(nums[i])
    print()


def test():
    t1 = [1, 1, 2]
    l1 = Solution().removeDuplicates(t1)
    assert l1 == 2
    printRet(t1, l1)
    t2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    l2 = Solution().removeDuplicates(t2)
    assert l2 == 5
    printRet(t2, l2)
