#!/usr/bin/env python
"""
CREATED AT: 2021/7/26
Des:
https://leetcode.com/problems/single-number/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/single-number/solution/
"""
import functools
import operator
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber2(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a

    def singleNumber3(self, nums: List[int]) -> int:
        """
        CREATED AT: 2022/2/15
        Runtime: 217 ms, faster than 38.95%
        Memory Usage: 16.8 MB, less than 10.15%
        1 <= nums.length <= 3 * 10^4
        -3 * 10^4 <= nums[i] <= 3 * 10^4
        Each element in the array appears twice except for one element which appears only once.
        """
        return functools.reduce(operator.xor, nums)


def test():
    assert Solution().singleNumber(nums=[2, 2, 1]) == 1
    assert Solution().singleNumber(nums=[4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber(nums=[1]) == 1

    assert Solution().singleNumber2(nums=[2, 2, 1]) == 1
    assert Solution().singleNumber2(nums=[4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber2(nums=[1]) == 1

    assert Solution().singleNumber3(nums=[2, 2, 1]) == 1
    assert Solution().singleNumber3(nums=[4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber3(nums=[1]) == 1


if __name__ == '__main__':
    test()
