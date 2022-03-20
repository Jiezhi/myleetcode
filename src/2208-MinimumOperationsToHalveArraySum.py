#!/usr/bin/env python
"""
CREATED AT: 2022/3/20
Des:

https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 🏆 Biweekly Contest 74

See: 

"""
import heapq
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^7
        """
        half = sum(nums) / 2
        nums = [-x for x in nums]
        heapq.heapify(nums)
        ret = 0
        while half > 0:
            head = heapq.heappop(nums)
            # head was negtive
            half += head / 2
            heapq.heappush(nums, head / 2)
            ret += 1
        return ret


def test():
    assert Solution().halveArray(nums=[5, 19, 8, 1]) == 3
    assert Solution().halveArray(nums=[3, 8, 20]) == 3


if __name__ == '__main__':
    test()
