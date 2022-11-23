#!/usr/bin/env python3
"""
CREATED AT: 2022-11-23

URL: https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1742-MaximumNumberOfBallsInABox

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        Runtime: 490 ms, faster than 92.16%
        Memory Usage: 13.8 MB, less than 97.97%
        1 <= lowLimit <= highLimit <= 10^5
        """

        def get_box(num) -> int:
            ret = 0
            while num >= 10:
                num, left = divmod(num, 10)
                ret += left
            return ret + num

        cnt = Counter()
        for num in range(lowLimit, highLimit + 1):
            cnt[get_box(num)] += 1
        return cnt.most_common(1)[0][1]


def test():
    assert Solution().countBalls(lowLimit=1, highLimit=10) == 2
    assert Solution().countBalls(lowLimit=5, highLimit=15) == 2
    assert Solution().countBalls(lowLimit=19, highLimit=28) == 2


if __name__ == '__main__':
    test()
