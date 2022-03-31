#!/usr/bin/env python
"""
CREATED AT: 2022/3/31
Des:
https://leetcode.com/problems/split-array-largest-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
from functools import lru_cache
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        1 <= nums.length <= 1000
        0 <= nums[i] <= 10^6
        1 <= m <= min(50, nums.length)
        """

        if m == 1:
            return sum(nums)
        acc = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            acc[i + 1] = acc[i] + nums[i]
        large_num = 2 ** 31

        @lru_cache(None)
        def dp(pos, m) -> int:
            if pos >= len(acc) or m > len(acc) - pos:
                return large_num
            if m == len(nums) - pos:
                return max(nums[pos:])
            if m == 1:
                return acc[-1] - acc[pos]
            ret = acc[-1]
            for i in range(1, len(acc) - pos):
                first = acc[pos + i] - acc[pos]
                max_ret = max(first, dp(pos + i, m - 1))
                ret = min(ret, max_ret)
                if first >= ret:
                    break
            return ret

        return dp(0, m)


def test():
    assert Solution().splitArray([7, 2, 5, 10, 8], 2) == 18


if __name__ == '__main__':
    test()
