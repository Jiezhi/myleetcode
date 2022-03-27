#!/usr/bin/env python
"""
CREATED AT: 2022/3/27
Des:
https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^5
        """
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            else:
                if len(stack) % 2 == 1 and stack[-1] == num:
                    continue
                else:
                    stack.append(num)
        if len(stack) % 2 == 1:
            stack.pop()
        return len(nums) - len(stack)


def test():
    assert Solution().minDeletion(nums=[1, 1, 2, 3, 5]) == 1
    assert Solution().minDeletion(nums=[1, 1, 2, 2, 3, 3]) == 2


if __name__ == '__main__':
    test()
