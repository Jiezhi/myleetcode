#!/usr/bin/env python
"""
CREATED AT: 2022/2/28
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Runtime: 43 ms, faster than 50.47%
        Memory Usage: 14 MB, less than 61.40%
        0 <= nums.length <= 20
        -2^31 <= nums[i] <= 2^31 - 1
        All the values of nums are unique.
        nums is sorted in ascending order.
        """
        if not nums:
            return []
        ret = []

        tmp_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                continue

            if nums[i - 1] == tmp_num:
                ret.append(f'{tmp_num}')
            else:
                ret.append(f'{tmp_num}->{nums[i - 1]}')
            tmp_num = nums[i]
        if tmp_num == nums[-1]:
            ret.append(f'{tmp_num}')
        else:
            ret.append(f'{tmp_num}->{nums[-1]}')
        return ret


def test():
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]


if __name__ == '__main__':
    test()
