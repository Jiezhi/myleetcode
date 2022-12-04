#!/usr/bin/env python3
"""
CREATED AT: 2022-12-04

URL: https://leetcode.com/problems/minimum-average-difference/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2256-MinimumAverageDifference

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """
        Runtime: 2593 ms, faster than 43.87%
        Memory Usage: 26.4 MB, less than 17.74%

        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^5
        """
        n = len(nums)
        acc = list(itertools.accumulate(nums))
        ret = [-1, 10 ** 5]
        for i, a in enumerate(acc[:-1]):
            r = abs(int(acc[i] / (i + 1)) - int((acc[-1] - acc[i]) / (n - i - 1)))
            if r < ret[1]:
                ret = [i, r]
        if acc[-1] / n < ret[1]:
            return n - 1
        return ret[0]


def test():
    assert Solution().minimumAverageDifference(nums=[0, 1, 0, 1, 0, 1]) == 0
    assert Solution().minimumAverageDifference(nums=[2, 5, 3, 9, 5, 3]) == 3
    assert Solution().minimumAverageDifference(nums=[0]) == 0


if __name__ == '__main__':
    test()
