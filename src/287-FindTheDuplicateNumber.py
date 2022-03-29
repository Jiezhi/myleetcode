#!/usr/bin/env python
"""
CREATED AT: 2022/3/29
Des:
https://leetcode.com/problems/find-the-duplicate-number/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Ref: https://leetcode.com/problems/find-the-duplicate-number/solution/
        Runtime: 778 ms, faster than 64.60%
        Memory Usage: 28 MB, less than 33.67%

        1 <= n <= 10^5
        nums.length == n + 1
        1 <= nums[i] <= n
        All the integers in nums appear only once except for precisely one integer which appears two or more times.
        """
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast


def test():
    pass


if __name__ == '__main__':
    test()
