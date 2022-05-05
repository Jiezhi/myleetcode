#!/usr/bin/env python
"""
CREATED AT: 2022/5/5
Des:
https://leetcode.com/problems/wiggle-subsequence/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from functools import lru_cache
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Runtime: 1163 ms, faster than 5.15%
        Memory Usage: 175 MB, less than 5.46%

        :param nums: 1 <= nums.length <= 1000
                    0 <= nums[i] <= 1000
        :return:
        """
        n = len(nums)
        if n <= 1:
            return n

        @lru_cache(None)
        def dp(i, j, incre) -> int:
            if j >= n or i >= n:
                return 0
            ret = dp(i, j + 1, incre)
            if incre and nums[j] > nums[i]:
                ret = max(1 + dp(j, j + 1, False), ret)
            elif not incre and nums[j] < nums[i]:
                ret = max(ret, 1 + dp(j, j + 1, True))
            return ret

        return max(max(dp(i, i + 1, True), dp(i, i + 1, False)) for i in range(n - 1)) + 1


def test():
    assert Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert Solution().wiggleMaxLength(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2


if __name__ == '__main__':
    test()
