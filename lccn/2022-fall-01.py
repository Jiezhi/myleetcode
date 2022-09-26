#!/usr/bin/env python
"""
CREATED AT: 2022/9/26
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

URL: https://leetcode.cn/contest/season/2022-fall/problems/6CE719/
https://leetcode.cn/problems/6CE719/

Tag: 

See: 

"""
from typing import List


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        """
        2 <= temperatureA.length == temperatureB.length <= 1000
        -20 <= temperatureA[i], temperatureB[i] <= 40
        """
        ret = 0
        cur = 0
        for i in range(1, len(temperatureA)):
            if temperatureA[i] == temperatureA[i - 1] and temperatureB[i] == temperatureB[i - 1]:
                cur += 1
            elif (temperatureA[i] - temperatureA[i - 1]) * (temperatureB[i] - temperatureB[i - 1]) > 0:
                cur += 1
            else:
                cur = 0
            ret = max(ret, cur)
        return ret


def test():
    assert Solution().temperatureTrend(
        temperatureA=[21, 18, 18, 18, 31],
        temperatureB=[34, 32, 16, 16, 17]) == 2


if __name__ == '__main__':
    test()
