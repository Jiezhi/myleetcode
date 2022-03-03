#!/usr/bin/env python
"""
CREATED AT: 2022/3/3
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Ref: https://leetcode.com/problems/longest-consecutive-sequence/solution/
        Runtime: 298 ms, faster than 62.88%
        Memory Usage: 27.7 MB, less than 29.96%

        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        """
        if not nums:
            return 0
        num_set = set(nums)
        ret = 1
        tmp_ret = 1
        for num in num_set:
            if num - 1 in num_set:
                continue
            tmp_num = num
            while tmp_num + 1 in num_set:
                tmp_num += 1
                tmp_ret += 1

            ret = max(ret, tmp_ret)
            tmp_ret = 1

        return ret


def test():
    assert Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


if __name__ == '__main__':
    test()
