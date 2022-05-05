#!/usr/bin/env python
"""
CREATED AT: 2022/5/5
Des:
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP

See: 

"""
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        Runtime: 640 ms, faster than 90.36%
        Memory Usage: 27.6 MB, less than 92.08%

        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        """

        ret, neg_ret, pos_ret = 0, 0, 0
        for num in nums:
            if num == 0:
                pos_ret = 0
                neg_ret = 0
            elif num < 0:
                if neg_ret > 0:
                    pos_ret, neg_ret = neg_ret + 1, pos_ret + 1
                else:
                    neg_ret = pos_ret + 1
                    pos_ret = 0
            else:
                if neg_ret > 0:
                    neg_ret += 1
                pos_ret += 1
            ret = max(ret, pos_ret)
        return ret


def test():
    assert Solution().getMaxLen(nums=[1, -2, -3, 4]) == 4
    assert Solution().getMaxLen(nums=[0, 1, -2, -3, -4]) == 3


if __name__ == '__main__':
    test()
