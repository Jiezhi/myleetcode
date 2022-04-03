#!/usr/bin/env python
"""
CREATED AT: 2022/4/3
Des:
https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        """
        current and correct are in the format "HH:MM"
        current <= correct
        """
        sh, sm = current.split(':')
        th, tm = correct.split(':')
        source = int(sh) * 60 + int(sm)
        target = int(th) * 60 + int(tm)

        diff = target - source

        ret = 0
        cnt, diff = divmod(diff, 60)
        ret += cnt
        cnt, diff = divmod(diff, 15)
        ret += cnt
        cnt, diff = divmod(diff, 5)
        ret += cnt
        ret += diff
        return ret


def test():
    assert Solution().convertTime(current="02:30", correct="04:35") == 3


if __name__ == '__main__':
    test()
