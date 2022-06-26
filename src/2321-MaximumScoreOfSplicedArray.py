#!/usr/bin/env python3
"""
CREATED AT: 2022-06-26

URL:https://leetcode.com/problems/maximum-score-of-spliced-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2321-MaximumScoreOfSplicedArray

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        """
        n == nums1.length == nums2.length
        1 <= n <= 10^5
        1 <= nums1[i], nums2[i] <= 10^4
        :param nums1:
        :param nums2:
        :return:
        """
        n = len(nums1)
        diff = [nums1[i] - nums2[i] for i in range(n)]

        sum1, sum2 = sum(nums1), sum(nums2)

        ret = max(sum1, sum2)

        max_sub_diff, min_sub_diff = 0, 0
        tmp_max_diff, tmp_min_diff = 0, 0

        for d in diff:
            if tmp_max_diff + d < 0:
                tmp_max_diff = 0
            else:
                tmp_max_diff += d

            if tmp_min_diff + d > 0:
                tmp_min_diff = 0
            else:
                tmp_min_diff += d

            max_sub_diff = max(max_sub_diff, tmp_max_diff)
            min_sub_diff = min(min_sub_diff, tmp_min_diff)

        return max(ret, sum1 - min_sub_diff, sum2 + max_sub_diff)


def test():
    assert Solution().maximumsSplicedArray(nums1=[60, 60, 60], nums2=[10, 90, 10]) == 210
    assert Solution().maximumsSplicedArray(nums1=[20, 40, 20, 70, 30], nums2=[50, 20, 50, 40, 20]) == 220


if __name__ == '__main__':
    test()
