#!/usr/bin/env python3
"""
CREATED AT: 2022-09-25

URL: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2419-LongestSubarrayWithMaximumBitwiseAND

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^6
        """
        max_num = max(nums)
        pre = 0
        ret = 0
        for i, num in enumerate(nums):
            if num == max_num:
                ret = max(ret, i - pre + 1)
            else:
                pre = i + 1
        return ret


def test():
    assert Solution().longestSubarray(nums=[1, 2, 3, 3, 2, 2]) == 2
    assert Solution().longestSubarray(nums=[1, 2, 3, 4]) == 1


if __name__ == '__main__':
    test()
