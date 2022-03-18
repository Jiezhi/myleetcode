#!/usr/bin/env python
"""
CREATED AT: 2022/3/18
Des:
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        Runtime: 95 ms, faster than 78.47%
        Memory Usage: 13.9 MB, less than 35.62%

        1 <= nums.length <= 200
        1 <= nums[i] <= 100
        1 <= k <= 99
        """
        ret = 0
        cnt = collections.Counter(nums)
        for num in set(nums):
            if num + k in cnt:
                ret += cnt[num] * cnt[num + k]
        return ret


def test():
    assert Solution().countKDifference(nums=[1, 2, 2, 1], k=1) == 4
    assert Solution().countKDifference(nums=[1, 3], k=3) == 0


if __name__ == '__main__':
    test()
