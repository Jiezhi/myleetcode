#!/usr/bin/env python3
"""
CREATED AT: 2022-10-17

URL: https://leetcode.com/problems/fruit-into-baskets/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 904-FruitIntoBaskets

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Runtime: 1045 ms, faster than 86.91%
        Memory Usage: 20.3 MB, less than 31.46%
        1 <= fruits.length <= 10^5
        0 <= fruits[i] < fruits.length
        """
        stat = []
        fruits.append(-1)
        pre = (-1, 0)
        for i, f in enumerate(fruits):
            if f == pre[0]:
                continue
            stat.append((pre[0], i - pre[1]))
            pre = (f, i)
        ret = stat[1][1]
        i = 1
        while i < len(stat) - 1:
            cur = (stat[i][0], stat[i + 1][0])
            tmp = stat[i][1] + stat[i + 1][1]
            j = i + 2
            while j < len(stat):
                if stat[j][0] in cur:
                    tmp += stat[j][1]
                    j += 1
                else:
                    break
            ret = max(ret, tmp)
            i = j - 1
        return ret


def test():
    assert Solution().totalFruit(fruits=[1, 2, 1]) == 3
    assert Solution().totalFruit(fruits=[0, 1, 2, 2]) == 3
    assert Solution().totalFruit(fruits=[1, 2, 3, 2, 2]) == 4


if __name__ == '__main__':
    test()
