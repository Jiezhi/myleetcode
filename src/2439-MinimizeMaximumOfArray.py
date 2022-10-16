#!/usr/bin/env python3
"""
CREATED AT: 2022-10-16

URL: https://leetcode.com/problems/minimize-maximum-of-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2439-MinimizeMaximumOfArray

Difficulty: 

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        n == nums.length
        2 <= n <= 10^5
        0 <= nums[i] <= 10^9
        """
        n, s = len(nums), sum(nums)

        i = n - 1
        while i > 0:
            pre_avg = s // (i + 1)
            if nums[i] > pre_avg:
                diff = nums[i] - pre_avg
                nums[i - 1] += diff
                nums[i] -= diff
            s -= nums[i]
            i -= 1
        return max(nums)


def test():
    assert Solution().minimizeArrayValue(nums=[3, 7, 1, 6]) == 5


if __name__ == '__main__':
    test()
