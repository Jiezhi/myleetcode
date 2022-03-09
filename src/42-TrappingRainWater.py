#!/usr/bin/env python
"""
CREATED AT: 2022/3/9
Des:

https://leetcode.com/problems/trapping-rain-water/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Runtime: 128 ms, faster than 48.91%
        Memory Usage: 16.3 MB, less than 6.33%

        n == height.length
        1 <= n <= 2 * 10^4
        0 <= height[i] <= 10^5
        """

        def calc(left, right) -> int:
            if right[0] == left[0] + 1:
                return 0
            area = (right[0] - left[0] - 1) * min(left[1], right[1])
            for h in height[left[0] + 1: right[0]]:
                area -= h
            return area

        if not height:
            return 0

        incre_list = [(0, height[0])]
        max_height = height[0]
        for i in range(1, len(height)):
            if height[i] >= max_height:
                incre_list.append((i, height[i]))
                max_height = height[i]

        ret = 0
        for i in range(len(incre_list) - 1):
            ret += calc(incre_list[i], incre_list[i + 1])

        if incre_list[-1][0] < len(height) - 1:
            ret += self.trap(height[incre_list[-1][0]:][::-1])

        return ret


def test():
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 3]) == 1


if __name__ == '__main__':
    test()
