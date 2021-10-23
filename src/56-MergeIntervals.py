#!/usr/bin/env python
"""
CREATED AT: 2021/9/8
Des:

https://leetcode.com/problems/merge-intervals
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        168 / 168 test cases passed.
        Status: Accepted
        Runtime: 76 ms
        Memory Usage: 16.1 MB
        :param intervals:
        :return:
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = []
        tmp = intervals[0]
        for interval in intervals[1:]:
            if interval[1] < tmp[1]:
                continue
            if interval[0] <= tmp[1]:
                tmp[1] = interval[1]
            else:
                # interval[0] > tmp[1]
                ret.append(tmp)
                tmp = interval
        ret.append(tmp)
        return ret


def test():
    assert Solution().merge(intervals=[[1, 1]]) == [[1, 1]]
    assert Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]


if __name__ == '__main__':
    test()
