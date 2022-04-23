#!/usr/bin/env python
"""
CREATED AT: 2022/4/22
Des:
https://leetcode.com/problems/rotate-function/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Runtime: 1820 ms, faster than 42.12%
        Memory Usage: 23.3 MB, less than 36.36%

        n == nums.length
        1 <= n <= 10^5
        -100 <= nums[i] <= 100
        """
        ret, n, num_sum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            ret += i * num
        pre = ret
        for i in range(n - 1, 0, -1):
            pre += num_sum - nums[i] * n
            ret = max(ret, pre)
        return ret


def test():
    assert Solution().maxRotateFunction([4, 3, 2, 6]) == 26
    Solution().maxRotateFunction(list(range(-100, 100)))


if __name__ == '__main__':
    test()
