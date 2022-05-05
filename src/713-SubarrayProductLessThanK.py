#!/usr/bin/env python
"""
CREATED AT: 2022/5/5
Des:
https://leetcode.com/problems/subarray-product-less-than-k/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Runtime: 913 ms, faster than 48.89%
        Memory Usage: 16.7 MB, less than 27.46%

        1 <= nums.length <= 3 * 10^4
        1 <= nums[i] <= 1000
        0 <= k <= 10^6
        """
        ret = 0
        i, j, p = 0, 0, 1
        while i < len(nums):
            if j < i:
                j = i
                p = 1
            while j < len(nums) and p * nums[j] < k:
                p *= nums[j]
                j += 1
            ret += j - i
            p //= nums[i]
            i += 1
        return ret


def test():
    assert Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert Solution().numSubarrayProductLessThanK([1, 2, 3], 0) == 0


if __name__ == '__main__':
    test()
