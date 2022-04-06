#!/usr/bin/env python
"""
CREATED AT: 2022/4/6
Des:
https://leetcode.com/problems/non-overlapping-intervals/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Runtime: 1521 ms, faster than 82.57%
        Memory Usage: 52.9 MB, less than 42.12%

        1 <= intervals.length <= 10^5
        intervals[i].length == 2
        -5 * 10^4 <= starti < endi <= 5 * 10^4
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = 0
        pre_end = intervals[0][0] - 1
        for start, end in intervals:
            if start >= pre_end:
                pre_end = end
            else:
                # remove the one with the largest end
                pre_end = min(pre_end, end)
                ret += 1
        return ret


def test():
    assert Solution().eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert Solution().eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2


if __name__ == '__main__':
    test()
