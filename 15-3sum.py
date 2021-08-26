#!/usr/bin/env python
"""
https://leetcode.com/problems/3sum/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
Created on 2018-12-17
Updated on 2021-08-25

@author: 'Jiezhi.G@gmail.com'

Reference: https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        20210825

        318 / 318 test cases passed.
        Status: Accepted
        Runtime: 1062 ms
        Memory Usage: 17.6 MB
        :param nums:
        :return:
        """

        n = len(nums)
        if n <= 2:
            return []
        nums = sorted(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        ret = []
        last_value = nums[0] - 1
        for i in range(n - 2):
            # sorted array and nums[i] > 0 means no more solutions
            if nums[i] > 0:
                return ret

            # skip duplicate value
            if nums[i] == last_value:
                continue
            last_value = nums[i]

            low, high = i + 1, n - 1
            left = -nums[i]
            while low < high:
                if nums[low] + nums[high] == left:
                    ret.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                if nums[low] + nums[high] > left:
                    high -= 1
                else:
                    low += 1
        return ret


def test():
    ans = [[-1, 0, 1], [-1, -1, 2]]
    ret = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret

    ans = [[-15, 1, 14], [-15, 3, 12], [-15, 4, 11], [-15, 5, 10], [-15, 6, 9], [-15, 7, 8], [-14, 0, 14], [-14, 2, 12],
           [-14, 3, 11], [-14, 4, 10], [-14, 5, 9], [-14, 6, 8], [-14, 7, 7], [-13, -1, 14], [-13, 1, 12], [-13, 2, 11],
           [-13, 3, 10], [-13, 4, 9], [-13, 5, 8], [-13, 6, 7], [-12, -2, 14], [-12, 0, 12], [-12, 1, 11], [-12, 2, 10],
           [-12, 3, 9], [-12, 4, 8], [-12, 5, 7], [-12, 6, 6], [-11, -3, 14], [-11, -1, 12], [-11, 0, 11], [-11, 1, 10],
           [-11, 2, 9], [-11, 3, 8], [-11, 4, 7], [-11, 5, 6], [-9, -5, 14], [-9, -3, 12], [-9, -2, 11], [-9, -1, 10],
           [-9, 0, 9], [-9, 1, 8], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, -6, 14], [-8, -4, 12], [-8, -3, 11],
           [-8, -2, 10],
           [-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-8, 4, 4], [-7, -7, 14], [-7, -5, 12],
           [-7, -4, 11],
           [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], [-7, 0, 7], [-7, 1, 6], [-7, 2, 5], [-7, 3, 4], [-6, -6, 12],
           [-6, -5, 11],
           [-6, -4, 10], [-6, -3, 9], [-6, -2, 8], [-6, -1, 7], [-6, 0, 6], [-6, 1, 5], [-6, 2, 4], [-6, 3, 3],
           [-5, -5, 10],
           [-5, -4, 9], [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -4, 8],
           [-4, -3, 7],
           [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-3, -3, 6], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3],
           [-3, 1, 2],
           [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1], [0, 0, 0]]
    ret = Solution().threeSum(
        [5, -11, -7, -2, 4, 9, 4, 4, -5, 12, 12, -14, -5, 3, -3, -2, -6, 3, 3, -9, 4, -13, 6, 2, 11, 12, 10, -14, -15,
         11, 0, 5, 8, 0, 10, -11, -6, -1, 0, 4, -4, -3, 5, -2, -15, 9, 11, -13, -2, -8, -7, 9, -6, 7, -11, 12, 4, 14, 6,
         -4, 3, -9, -14, -12, -2, 3, -8, 7, -13, 7, -12, -9, 11, 0, 4, 12, -6, -7, 14, -1, 0, 14, -6, 1, 6, -2, -9, -4,
         -11, 12, -1, -1, 10, -7, -6, -7, 11, 1, -15, 6, -15, -12, 12, 12, 3, 1, 9, 12, 9, 0, -11, -14, -1])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret


if __name__ == '__main__':
    test()
