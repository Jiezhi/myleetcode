#!/usr/bin/env python
"""
CREATED AT: 2022/3/4
Des:

https://leetcode.com/problems/champagne-tower/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Runtime: 100 ms, faster than 92.23%
        Memory Usage: 14.1 MB, less than 67.48%

        0 <= poured <= 10^9
        0 <= query_glass <= query_row < 100
        """
        tower = [[0] * i for i in range(1, 101)]

        tower[0][0] = poured
        for i in range(query_row):
            flow = False
            for j in range(i + 1):
                if tower[i][j] > 1:
                    flow = True
                    flow_down = tower[i][j] - 1
                    tower[i + 1][j] += 0.5 * flow_down
                    tower[i + 1][j + 1] += 0.5 * flow_down
            if not flow:
                break

        ret = tower[query_row][query_glass]
        return 1 if ret >= 1 else ret


def test():
    pass


if __name__ == '__main__':
    test()
