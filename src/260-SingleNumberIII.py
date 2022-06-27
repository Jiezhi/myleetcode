#!/usr/bin/env python
"""
CREATED AT: 2021/11/6
Des:

https://leetcode.com/problems/single-number-iii/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/single-number-iii/discuss/1561785/

Difficulty: Medium

Tag: Math, Bits

See: LCOF40
"""
from functools import reduce
from typing import List

from tool import print_results, equal_list_value


class Solution:
    @print_results
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Runtime: 48 ms, faster than 99.76%
        Memory Usage: 15.8 MB, less than 84.86%
        
        2 <= nums.length <= 3 * 10^4
        -2^31 <= nums[i] <= 2^31 - 1
        Each integer in nums will appear twice, only two integers will appear once.
        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return []

        if len(nums) == 2 and nums[0] != nums[1]:
            return nums

        ret = reduce(lambda x, y: x ^ y, nums)

        right_bit = ret & -ret
        ret2 = 0
        for num in nums:
            if (right_bit & num) != 0:
                ret2 ^= num
        return [ret2, ret ^ ret2]


def test():
    assert equal_list_value(Solution().singleNumber(nums=[1, 2, 1, 3, 2, 5]), [3, 5])
    assert equal_list_value(Solution().singleNumber(nums=[-1, 0]), [-1, 0])


if __name__ == '__main__':
    test()
