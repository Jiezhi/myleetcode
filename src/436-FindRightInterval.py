#!/usr/bin/env python3
"""
CREATED AT: 2022-06-16

URL: https://leetcode.com/problems/find-right-interval/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 436-FindRightInterval

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        Runtime: 377 ms, faster than 75.25%
        Memory Usage: 20.2 MB, less than 32.78%

        1 <= intervals.length <= 2 * 10^4
        intervals[i].length == 2
        -10^6 <= starti <= endi <= 10^6
        The start point of each interval is unique.
        """
        ends = sorted((x[0], i) for i, x in enumerate(intervals))
        end, pos = [], []
        for i, j in ends:
            end.append(i)
            pos.append(j)

        ret = []
        for _, e in intervals:
            p = bisect.bisect_left(end, e)
            if p >= len(pos):
                ret.append(-1)
            else:
                ret.append(pos[p])
        return ret


def test():
    assert Solution().findRightInterval(intervals=[[1, 2]]) == [-1]
    assert Solution().findRightInterval(intervals=[[3, 4], [2, 3], [1, 2]]) == [-1, 0, 1]


if __name__ == '__main__':
    test()
