#!/usr/bin/env python3
"""
CREATED AT: 2022-10-19

URL: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1700-NumberOfStudentsUnableToEatLunch

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Runtime: 42 ms, faster than 89.16%
        Memory Usage: 13.8 MB, less than 71.25%

        1 <= students.length, sandwiches.length <= 100
        students.length == sandwiches.length
        sandwiches[i] is 0 or 1.
        students[i] is 0 or 1.
        """
        cnt = Counter(students)
        for s in sandwiches:
            if cnt[s]:
                cnt[s] -= 1
            else:
                break
        return cnt[0] + cnt[1]


def test():
    assert Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]) == 0
    assert Solution().countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]) == 3


if __name__ == '__main__':
    test()
