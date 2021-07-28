#!/usr/bin/env python
"""
CREATED AT: 2021/7/28
Des:
https://leetcode.com/problems/3sum-closest/
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/3sum-closest/solution/
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        close_sum = nums[0] + nums[1] + nums[2]
        if len(nums) == 3:
            return close_sum
        l = len(nums)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    tmp_sum = nums[i] + nums[j] + nums[k]
                    if tmp_sum == target:
                        return tmp_sum
                    if abs(target - close_sum) > abs(target - tmp_sum):
                        close_sum = tmp_sum
        return close_sum

    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        """
        131 / 131 test cases passed.
        Status: Accepted
        Runtime: 124 ms
        Memory Usage: 14.4 MB
        :param nums:
        :param target:
        :return:
        """
        close_sum = nums[0] + nums[1] + nums[2]
        diff = abs(target - close_sum)
        if len(nums) == 3:
            return close_sum
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == target:
                    return tmp_sum
                elif tmp_sum > target:
                    k -= 1
                else:
                    j += 1
                if diff > abs(target - tmp_sum):
                    close_sum = tmp_sum
                    diff = abs(target - tmp_sum)
        return close_sum


def test():
    assert Solution().threeSumClosest2(nums=[-1, 2, 1, -4], target=1) == 2
    assert Solution().threeSumClosest2(nums=[2, 1, -4], target=1) == -1
    assert Solution().threeSumClosest2([1, 1, 1, 0], -100) == 2
    nums = [85, 17, 99, 58, 76, -80, 68, -38, -74, -75, -88, -31, 17, -2, -40, -57, 29, -84, -16, -31, -80, -39, 58,
            -33,
            67, 11, 38, 2, -31, -48, -29, 28, -11, -52, 86, -86, 59, 45, 68, 15, -17, 56, 34, 8, 29, 69, -93, 84, -76,
            -98,
            85, 59, 40, -93, -47, -9, 100, 51, 55, 31, -47, -9, -63, -9, -94, 32, 21, 88, 60, 36, -54, 2, 42, 86, -44,
            -81,
            -82, -29, -48, 49, 77, -19, 3, 26, -53, 35, 39, 92, -56, 77, -59, 56, -13, 18, -56, -70, 81, 31, -28, -13,
            -51,
            19, 86, 36, 20, 7, -2, -52, -14, -10, -70, 3, -34, 100, 90, 75, -27, -62, -37, -19, 42, 68, -56, -94, 22,
            -6,
            49, -74, 76, -11, -18, -71, -46, 23, 62, -72, 35, 82, 92, 27, -10, -38, -9, 7, -18, -83, -37, 48, -18, 98,
            -80,
            16, 6, -72, -4, 45, -99, 39, 27, -24, 31, -48, 26, 16, 32, -56, -14, 94, -36, 86, 30, -21, 45, -68, -74, 50,
            -65, 39, -25, 67, 1, -36, 61, -2, 60, 71, -16]

    assert Solution().threeSumClosest2(nums, 67) == 67


if __name__ == '__main__':
    test()
