#!/usr/bin/env python
"""
CREATED AT: 2022/2/28
Des:

https://leetcode.com/problems/remove-covered-intervals/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Optimized Solution: https://github.com/Jiezhi/LCOF-Java/blob/main/src/main/java/io/github/jiezhi/lc/LC1288.java

Time Spent:  min
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Runtime: 224 ms, faster than 8.79%
        Memory Usage: 14.3 MB, less than 90.42%

        1 <= intervals.length <= 1000
        intervals[i].length == 2
        0 <= li <= ri <= 10^5
        All the given intervals are unique.
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        ret = n
        for i in range(n):
            node = intervals[i]
            j = 0
            while j < n and intervals[j][0] <= node[0]:
                if j == i:
                    j += 1
                    continue
                if intervals[j][1] >= node[1]:
                    ret -= 1
                    break
                j += 1
        return ret


def test():
    assert Solution().removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]) == 2


if __name__ == '__main__':
    test()
