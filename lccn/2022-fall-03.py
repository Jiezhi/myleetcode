#!/usr/bin/env python
"""
CREATED AT: 2022/9/26
Des:

GITHUB: https://github.com/Jiezhi/myleetcode
URL: https://leetcode.cn/problems/EXvqDp/
https://leetcode.cn/contest/season/2022-fall/problems/EXvqDp/

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        """
        1 <= num <= 10^6
        1 <= plate.length, plate[i].length <= 1000
        plate[i][j] 仅包含 "O"、"W"、"E"、"."
        """
        ret, stack = [], []
        m, n = len(plate), len(plate[0])

        seen = {}

        dir_dict = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        dirs = ['U', 'R', 'D', 'L']

        def dfs(x, y, d) -> (int, bool):
            if not 0 <= x < m or not 0 <= y < n:
                return -1, False
            if plate[x][y] == 'O':
                return 0, True
            if (x, y, d) in seen:
                return seen[(x, y, d)]
            seen[(x, y, d)] = (-1, False)
            new_d = d
            if plate[x][y] == 'E':
                new_d = dirs[(dirs.index(d) + 1) % 4]
            elif plate[x][y] == 'W':
                new_d = dirs[(dirs.index(d) - 1) % 4]
            cnt, can = dfs(x + dir_dict[new_d][0], y + dir_dict[new_d][1], new_d)
            if can:
                seen[(x, y, d)] = (cnt + 1, True)
            return seen[(x, y, d)]

        for i in range(1, m - 1):
            if plate[i][0] == '.':
                cnt, can = dfs(i, 0, 'R')
                if can and cnt <= num:
                    ret.append([i, 0])

            if plate[i][n - 1] == '.':
                cnt, can = dfs(i, n - 1, 'L')
                if can and cnt <= num:
                    ret.append([i, n - 1])

        for j in range(1, n - 1):
            if plate[0][j] == '.':
                cnt, can = dfs(0, j, 'D')
                if can and cnt <= num:
                    ret.append([0, j])

            if plate[m - 1][j] == '.':
                cnt, can = dfs(m - 1, j, 'U')
                if can and cnt <= num:
                    ret.append([m - 1, j])

        return ret


def test():
    assert Solution().ballGame(num=4, plate=["..E.", ".EOW", "..W."]) == [[2, 1]]


if __name__ == '__main__':
    test()
