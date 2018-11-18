#!/usr/bin/env python
"""
https://leetcode.com/problems/merge-sorted-array/description/
Created on 2018-11-16

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        n1 = 0
        n2 = 0
        while n2 < n:
            # nums1 run out of number, just copy all left nums2 numbers
            if n1 >= m + n2:
                for i in range(n2, n):
                    nums1[n1 + i - n2] = nums2[i]
                return
            if nums1[n1] > nums2[n2]:
                for i in range(m + n2, n1, -1):
                    nums1[i] = nums1[i - 1]
                nums1[n1] = nums2[n2]
                n2 += 1
            n1 += 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]
