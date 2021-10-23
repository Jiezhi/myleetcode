#!/usr/bin/env python
"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
Created on 2018-11-24

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return getMedian(nums2)
        if not nums2:
            return getMedian(nums1)

        n1 = len(nums1)
        n2 = len(nums2)
        max_pos = (n1 + n2) // 2
        nums = [0] * (n1 + n2)
        i = 0
        j = 0
        while i < n1 and j < n2 and i + j <= max_pos:
            if nums1[i] < nums2[j]:
                nums[i + j] = nums1[i]
                i += 1
            else:
                nums[i + j] = nums2[j]
                j += 1
        if i == n1:
            nums[i + j: max_pos + 1] = nums2[j:max_pos - i + 1]
        elif j == n2:
            nums[i + j: max_pos + 1] = nums1[i:max_pos - j + 1]
        return getMedian(nums)

    # def findMedianSortedArrays2(self, nums1, nums2):
    #     """
    #     TODO 可以不用额外的数组来存储nums1和nums2重新排序后的数据，因为只要找到两数组长度的中间位置的数即可
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     n1 = len(nums1)
    #     n2 = len(nums2)
    #     if not n1:
    #         return getMedian(nums2)
    #     if not n2:
    #         return getMedian(nums1)
    #     i = 0
    #     j = 0
    #     mid_pos = (n1 + n2) // 2 - 1
    #
    #     while i + j < mid_pos:
    #         if nums1[i] < nums2[j]:
    #             i += 1
    #         else:
    #             j += 1
    #     if (n1 + n2) % 2:
    #         if nums1[i] < nums2[j]:
    #             tmp1 = nums1[i]
    #             i += 1
    #         else:
    #             tmp1 = nums2[j]
    #             j += 1
    #         tmp2 = min(nums1[i], nums2[j])
    #         return (tmp1 + tmp2) / 2
    #     else:
    #         if nums1[i] < nums2[j]:
    #             return min(nums1[i + 1], nums2[j])
    #         else:
    #             return min(nums1[i], nums2[j + 1])


def getMedian(nums):
    print(nums)
    if not len(nums) % 2:
        return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
    else:
        return nums[len(nums) // 2]


def test():
    assert Solution().findMedianSortedArrays([1, 2, 3], []) == 2
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert Solution().findMedianSortedArrays([1, 2, 3], []) == 2
    assert Solution().findMedianSortedArrays([1, 3], [2, 4]) == 2.5
    assert Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4]) == 4
    # assert Solution().findMedianSortedArrays2([1, 2, 3], []) == 2
    # assert Solution().findMedianSortedArrays2([1, 3], [2]) == 2
    # assert Solution().findMedianSortedArrays2([1, 2, 3], []) == 2
    # assert Solution().findMedianSortedArrays2([1, 3], [2, 4]) == 2.5
