#!/usr/bin/env python
"""
CREATED AT: 2022-06-07
Des: https://leetcode.com/problems/largest-rectangle-in-histogram/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Ref: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/452612/Thinking-Process-for-Stack-Solution
        98 / 98 test cases passed.
        Runtime: 1085 ms, faster than 77.13%
        Memory Usage: 30.6 MB, less than 24.02%
        :param heights:
        1 <= heights.length <= 10^5
        0 <= heights[i] <= 10^4
        :return:
        """
        ret = 0
        heights.append(0)
        mono_stack = [(-1, 0)]
        for i, v in enumerate(heights):
            while v < mono_stack[-1][1]:
                pre = mono_stack.pop()
                ret = max(ret, pre[1] * (i - mono_stack[-1][0] - 1))
            mono_stack.append((i, v))
        return ret


def test():
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert Solution().largestRectangleArea([2, 1, 2]) == 3
    assert Solution().largestRectangleArea([2, 4]) == 4


if __name__ == '__main__':
    test()
