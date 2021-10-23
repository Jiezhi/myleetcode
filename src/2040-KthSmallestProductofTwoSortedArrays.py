#!/usr/bin/env python
"""
CREATED AT: 2021/10/16
Des:
https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays
https://leetcode.com/contest/biweekly-contest-63/problems/kth-smallest-product-of-two-sorted-arrays/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 
"""
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        1 <= nums1.length, nums2.length <= 5 * 10**4
        -10**5 <= nums1[i], nums2[j] <= 10**5
        1 <= k <= nums1.length * nums2.length
        nums1 and nums2 are sorted.
        :param nums1:
        :param nums2:
        :param k:
        :return:
        """
        neg_1, neg_2, zero_1, zero_2 = 0, 0, 0, 0
        n1, n2 = len(nums1), len(nums2)
        i = 0
        while True:
            while i < n1 and nums1[i] < 0:
                neg_1 += 1
                i += 1
            while i < n1 and nums1[i] == 0:
                zero_1 += 1
                i += 1
            break
        i = 0
        while True:
            while i < n2 and nums2[i] < 0:
                neg_2 += 1
                i += 1
            while i < n2 and nums2[i] == 0:
                zero_2 += 1
                i += 1
            break
        pos_1, pos_2 = n1 - neg_1 - zero_1, n2 - neg_2 - zero_2
        neg_cnt = neg_1 * pos_2 + neg_2 * pos_1
        zero_cnt = zero_1 * n2 + zero_2 * n1
        pos_cnt = n1 * n2 - neg_cnt - zero_cnt

        if k <= neg_cnt:
            # find in neg
            neg_list = []
            for i in range(neg_1):
                for j in range(n2 - 1, n2 - pos_2 - 1, -1):
                    neg_list.append(nums1[i] * nums2[j])
            for i in range(neg_2):
                for j in range(n1 - 1, n1 - pos_1 - 1, -1):
                    neg_list.append(nums1[j] * nums2[i])
            neg_list = sorted(neg_list)
            return neg_list[k - 1]
        elif k <= neg_cnt + zero_cnt:
            return 0
        else:
            # find in pos
            pos_list = []
            for i in range(neg_1 + zero_1, n1):
                for j in range(neg_2 + zero_2, n2):
                    pos_list.append(nums1[i] * nums2[j])
            for i in range(neg_1):
                for j in range(neg_2):
                    pos_list.append(nums1[i] * nums2[j])
            pos_list = sorted(pos_list, reverse=True)
            return pos_list[n1 * n2 - k]


def test():
    assert Solution().kthSmallestProduct(nums1=[3], nums2=[-3], k=1) == -9
    assert Solution().kthSmallestProduct(nums1=[2, 5], nums2=[3, 4], k=2) == 8
    assert Solution().kthSmallestProduct(nums1=[-4, -2, 0, 3], nums2=[2, 4], k=6) == 0
    assert Solution().kthSmallestProduct(nums1=[-2, -1, 0, 1, 2], nums2=[-3, -1, 2, 4, 5], k=3) == -6


if __name__ == '__main__':
    test()
