#!/usr/bin/env python3
"""
CREATED AT: 2022-06-23

URL: https://leetcode.com/problems/course-schedule-iii/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 630-CourseScheduleIII

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
import heapq
from functools import lru_cache
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Runtime: 727 ms, faster than 95.65%
        Memory Usage: 19.9 MB, less than 79.40%

        1 <= courses.length <= 10^4
        1 <= durationi, lastDayi <= 10^4
        """
        courses = sorted(courses, key=lambda x: x[1])
        taken = []
        total = 0
        for d, e in courses:
            if total + d <= e:
                total += d
                heapq.heappush(taken, -d)
            elif taken and d < -taken[0] and total + taken[0] <= e:
                total += heapq.heapreplace(taken, -d)
        return len(taken)

    def scheduleCourse2(self, courses: List[List[int]]) -> int:
        """
        LTE
        1 <= courses.length <= 10^4
        1 <= durationi, lastDayi <= 10^4
        """
        courses = sorted(courses, key=lambda x: x[1])
        n = len(courses)

        @lru_cache(None)
        def dp(pos, end) -> int:
            if pos >= n:
                return 0
            ret = dp(pos + 1, end)
            if end + courses[pos][0] > courses[pos][1]:
                return ret
            return max(ret, 1 + dp(pos + 1, end + courses[pos][0]))

        return dp(0, 0)


def test():
    assert Solution().scheduleCourse(courses=[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
    assert Solution().scheduleCourse(courses=[[1, 2]]) == 1
    assert Solution().scheduleCourse(courses=[[3, 2], [4, 3]]) == 0


if __name__ == '__main__':
    test()
