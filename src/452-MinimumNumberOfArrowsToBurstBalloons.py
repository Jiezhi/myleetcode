#!/usr/bin/env python
"""
CREATED AT: 2022/1/13
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag:

See:

Time Spent:  min

Ref: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/93703/Share-my-explained-Greedy-solution
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Runtime: 2601 ms, faster than 5.02%
        Memory Usage: 58.9 MB, less than 83.67%

        1 <= points.length <= 10^5
        points[i].length == 2
        -2^31 <= xstart < xend <= 2^31 - 1
        :param points:
        :return:
        """
        points = sorted(points, key=lambda x: x[1])
        ret = 1
        i = 1
        cur_point = points[0]
        while i < len(points):
            if points[i][0] <= cur_point[1]:
                i += 1
                continue
            ret += 1
            cur_point = points[i]

        return ret


def test():
    assert Solution().findMinArrowShots(points=[[1, 2], [2, 4]]) == 1
    assert Solution().findMinArrowShots(points=[[1, 2], [3, 4]]) == 2
    assert Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]) == 2


if __name__ == '__main__':
    test()
