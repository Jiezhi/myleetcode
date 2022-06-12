#!/usr/bin/env python3
"""
CREATED AT: 2022-06-12

URL:https://leetcode.com/problems/maximum-erasure-value/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1695-MaximumErasureValue

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        62 / 62 test cases passed.
        Runtime: 2636 ms, faster than 14.89%
        Memory Usage: 27.1 MB, less than 97.81%
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4
        """
        ret, tmp_ret = nums[0], nums[0]
        s = set()
        s.add(nums[0])
        l, r = 0, 1
        while l < len(nums):
            if r >= len(nums):
                break
            while r < len(nums) and nums[r] not in s:
                s.add(nums[r])
                tmp_ret += nums[r]
                r += 1
            ret = max(tmp_ret, ret)
            s.remove(nums[l])
            tmp_ret -= nums[l]
            l += 1
        return ret


def test():
    pass


if __name__ == '__main__':
    test()
