#!/usr/bin/env python
"""
https://leetcode.com/problems/remove-element/description/
Created on 2018-11-12

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums) - 1
        i = 0
        while i <= l:
            if nums[i] == val:
                while nums[l] == val:
                    l -= 1
                    if l < i:
                        print(0)
                        return i
                nums[i] = nums[l]
                l -= 1
            i += 1
        print(i, nums)
        return i


if __name__ == '__main__':
    Solution().removeElement([3, 2, 2, 3], 3)
    Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    Solution().removeElement([1], 1)
    Solution().removeElement([2, 2, 2, 2, 2, 2], 2)
    Solution().removeElement([4, 5], 5)
    Solution().removeElement([3, 2, 2, 3], 3)
