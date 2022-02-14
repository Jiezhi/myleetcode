#!/usr/bin/env python
"""
CREATED AT: 2022/2/13
Des:

https://leetcode.com/problems/maximum-and-sum-of-array/
https://leetcode.com/contest/weekly-contest-280/problems/maximum-and-sum-of-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

Time Spent:  min
"""
from functools import lru_cache
from typing import List


class Solution:

    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """
        CREATED AT: 2022/2/14
        Runtime: 903 ms, faster than 50.00%
        Memory Usage: 26.3 MB, less than 50.00%

        n == nums.length
        1 <= numSlots <= 9
        1 <= n <= 2 * numSlots
        1 <= nums[i] <= 15
        """

        @lru_cache(None)
        def dfs(pos, slots) -> int:
            if pos == len(nums):
                return 0
            max_ret = 0
            for i in range(1, len(slots)):
                if int(slots[i]) > 0:
                    new_slots = f'{slots[:i]}{int(slots[i]) - 1}{slots[i + 1:]}'
                    ret = (nums[pos] & i) + dfs(pos + 1, new_slots)
                    if ret > max_ret:
                        max_ret = ret
            return max_ret

        slots = '2' * (numSlots + 1)

        return dfs(0, slots)

    def maximumANDSum2(self, nums: List[int], numSlots: int) -> int:
        """
        CREATED AT: 2022/2/13
        n == nums.length
        1 <= numSlots <= 9
        1 <= n <= 2 * numSlots
        1 <= nums[i] <= 15
        """

        def dfs(nums, slots) -> int:
            if not nums:
                return 0
            max_ret = 0
            for i in range(1, len(slots)):
                if slots[i] > 0:
                    slots[i] -= 1
                    ret = (nums[0] & i) + dfs(nums[1:], slots)
                    if ret > max_ret:
                        max_ret = ret
                    slots[i] += 1
            return max_ret

        slots = [2] * (numSlots + 1)

        return dfs(nums, slots)


def test():
    assert Solution().maximumANDSum(nums=[14, 7, 9, 8, 2, 4, 11, 1, 9], numSlots=8) == 40
    assert Solution().maximumANDSum(nums=[1, 2, 3, 4, 5, 6], numSlots=3) == 9
    assert Solution().maximumANDSum(nums=[1, 3, 10, 4, 7, 1], numSlots=9) == 24


if __name__ == '__main__':
    test()
