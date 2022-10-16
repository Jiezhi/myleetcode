#!/usr/bin/env python3
"""
CREATED AT: 2022-10-16

URL: https://leetcode.com/problems/number-of-valid-clock-times/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2437-NumberOfValidClockTimes

Difficulty: 

Desc: 

Tag: 

See: 

"""


class Solution:
    def countTime(self, time: str) -> int:
        ret = 1
        if time[0] == '?':
            if time[1] == '?':
                ret *= 24
            elif 0 <= int(time[1]) <= 3:
                ret *= 3
            else:
                ret *= 2
        elif time[1] == '?':
            if int(time[0]) == 2:
                ret *= 4
            else:
                ret *= 10

        if time[3] == '?':
            ret *= 6
        if time[4] == '?':
            ret *= 10
        return ret


def test():
    assert Solution().countTime(time="?5:00") == 2


if __name__ == '__main__':
    test()
