#!/usr/bin/env python3
"""
CREATED AT: 2022-08-19

URL: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1450-NumberOfStudentsDoingHomeworkAtAGivenTime

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
        Runtime: 67 ms, faster than 35.35%
        Memory Usage: 14 MB, less than 26.05%

        startTime.length == endTime.length
        1 <= startTime.length <= 100
        1 <= startTime[i] <= endTime[i] <= 1000
        1 <= queryTime <= 1000
        """
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))


def test():
    assert Solution().busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4) == 1
    assert Solution().busyStudent(startTime=[4], endTime=[4], queryTime=4) == 1


if __name__ == '__main__':
    test()
