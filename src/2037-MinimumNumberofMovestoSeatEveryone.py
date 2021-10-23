#!/usr/bin/env python
"""
CREATED AT: 2021/10/16
Des:
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone
https://leetcode.com/contest/biweekly-contest-63/problems/minimum-number-of-moves-to-seat-everyone
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        n == seats.length == students.length
        1 <= n <= 100
        1 <= seats[i], students[j] <= 100
        :param seats:
        :param students:
        :return:
        """
        ret = 0
        for seat, student in zip(sorted(seats), sorted(students)):
            ret += abs(seat - student)
        return ret


def test():
    assert Solution().minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]) == 4
    assert Solution().minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]) == 4
    assert Solution().minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]) == 7


if __name__ == '__main__':
    test()
