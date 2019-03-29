#!/usr/bin/env python
"""
https://leetcode.com/problems/3sum/
Created on 2018-12-17

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        ret = list()
        last_min = nums[i] - 1
        last_max = nums[j] + 1
        while i < j:
            if nums[i] == last_min:
                i += 1
                continue
            if nums[j] == last_max:
                j -= 1
                continue
            remain = -nums[i] - nums[j]
            if remain in nums[i + 1: j]:
                ret.append([nums[i], nums[j], remain])

            last_min = nums[i]
            last_max = nums[j]
            if remain < 0:
                i += 1
            else:
                j -= 1
        return ret

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = list()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                remain = -nums[i] - nums[j]
                if remain in nums[j + 1:]:
                    r = [nums[i], nums[j], remain]
                    if not inList(ret, r):
                        ret.append(r)
        return ret


def inList(rets, ret):
    for t in rets:
        if set(ret) == set(t):
            return True
    return False


def test():
    # assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum(
        [5, -11, -7, -2, 4, 9, 4, 4, -5, 12, 12, -14, -5, 3, -3, -2, -6, 3, 3, -9, 4, -13, 6, 2, 11, 12, 10, -14, -15,
         11, 0, 5, 8, 0, 10, -11, -6, -1, 0, 4, -4, -3, 5, -2, -15, 9, 11, -13, -2, -8, -7, 9, -6, 7, -11, 12, 4, 14, 6,
         -4, 3, -9, -14, -12, -2, 3, -8, 7, -13, 7, -12, -9, 11, 0, 4, 12, -6, -7, 14, -1, 0, 14, -6, 1, 6, -2, -9, -4,
         -11, 12, -1, -1, 10, -7, -6, -7, 11, 1, -15, 6, -15, -12, 12, 12, 3, 1, 9, 12, 9, 0, -11, -14, -1]))
    print(Solution().threeSum(
        [8, 5, 3, 9, 12, -9, 8, -9, 13, -10, -14, -13, 5, -15, -4, 2, 8, -11, -6, 12, 9, -15, 13, 11, 13, 13, 6, -12,
         -15, -4, -6, 0, -14, 5, -14, 5, 3, 2, 4, 2, 7, 5, 4, -10, -3, 7, 7, -9, 4, -14, 10, -2, -13, 8, -6, 7, -1, 7,
         11, -9, -12, -10, 6, 12, 10, 7, 2, -9, -6, 13, 8, 9, 3, -11, 14, -14, 11, -2, 14, 0, -1, 1, 6, -7, -5, 7, -14,
         9, 0, 4, 7, -5, 1, -2, 14, -3, 12, -6, -5, 14, -8, -12, 0, 3, -8, -1]))
