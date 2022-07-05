#!/usr/bin/env python3
"""
CREATED AT: 2022-07-05

URL: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 315-CountOfSmallerNumbersAfterSelf

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
import bisect
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Runtime: 5060 ms, faster than 30.67% 
        Memory Usage: 34.5 MB, less than 54.61% 

        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        """
        ret = []
        sorted_nums = []
        nums = nums[::-1]
        for num in nums:
            pos = bisect.bisect_left(sorted_nums, num)
            ret.append(pos)
            sorted_nums.insert(pos, num)
        return ret[::-1]


def test():
    assert Solution().countSmaller(nums=[5, 2, 6, 1]) == [2, 1, 1, 0]
    assert Solution().countSmaller(nums=[-1]) == [0]
    assert Solution().countSmaller(nums=[-1, -1]) == [0, 0]


if __name__ == '__main__':
    test()
