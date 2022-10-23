#!/usr/bin/env python3
"""
CREATED AT: 2022-10-23

URL: https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/
https://leetcode.com/contest/weekly-contest-316/problems/determine-if-two-events-have-conflict/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2446-DetermineIfTwoEventsHaveConflict

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        """
        evnet1.length == event2.length == 2.
        event1[i].length == event2[i].length == 5
        startTime1 <= endTime1
        startTime2 <= endTime2
        All the event times follow the HH:MM format.
        """

        def get_time(s):
            return int(s[:2]) * 60 + int(s[3:])

        e1a, e1b = get_time(event1[0]), get_time(event1[1])
        e2a, e2b = get_time(event2[0]), get_time(event2[1])
        return not (e1a <= e1b < e2a <= e2b or e2a <= e2b < e1a <= e1b)


def test():
    assert Solution().haveConflict(event1=["01:15", "02:00"], event2=["02:00", "03:00"])
    assert not Solution().haveConflict(event1=["10:00", "11:00"], event2=["14:00", "15:00"])


if __name__ == '__main__':
    test()
