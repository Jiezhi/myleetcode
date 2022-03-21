#!/usr/bin/env python
"""
Created on 2020/11/29

Des:  https://leetcode.com/problems/squares-of-a-sorted-array/

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

"""
from typing import List


class Solution:
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        """
        Update At: 03/21/2022 13:40
        Runtime: 373 ms, faster than 31.41%
        Memory Usage: 16.4 MB, less than 18.41%

        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        nums is sorted in non-decreasing order.
        """
        lo, hi = 0, len(nums) - 1
        ret = [0] * len(nums)
        pos = len(nums) - 1
        while lo <= hi:
            if abs(nums[lo]) > abs(nums[hi]):
                ret[pos] = nums[lo] * nums[lo]
                lo += 1
            else:
                ret[pos] = nums[hi] * nums[hi]
                hi -= 1
            pos -= 1
        return ret

    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x * x for x in A])


def test():
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sortedSquares2([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


if __name__ == '__main__':
    test()
