#!/usr/bin/env python
"""
CREATED AT: 2022/4/23
Des:
https://leetcode-cn.com/contest/season/2022-spring/problems/PTXy4P/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        """
        1 <= time.length <= 100
        1 <= time[i] <= 100
        1 <= fruits.length <= 10^3
        0 <= fruits[i][0] < time.length
        1 <= fruits[i][1] < 10^3
        1 <= limit <= 100
        """
        ret = 0
        for t, num in fruits:
            cnt, left = divmod(num, limit)
            if left:
                cnt += 1
            ret += cnt * time[t]
        return ret


def test():
    assert Solution().getMinimumTime(time=[2, 3, 2], fruits=[[0, 2], [1, 4], [2, 1]], limit=3) == 10


if __name__ == '__main__':
    test()
