#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/3

Leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/

"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        head = 0
        tmp_sum = 0
        tmp_len = 0
        for i in range(len(nums)):
            if nums[i] >= s:
                return 1
            tmp_sum += nums[i]
            if tmp_sum >= s and tmp_len == 0:
                tmp_len = len(nums)
            while tmp_sum >= s:
                tmp_len = min(tmp_len, i - head + 1)
                tmp_sum -= nums[head]
                head += 1
        return tmp_len


def test():
    assert Solution().minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 2
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 1]) == 3
    assert Solution().minSubArrayLen(100, []) == 0
    assert Solution().minSubArrayLen(3, [1, 1]) == 0


if __name__ == '__main__':
    test()
