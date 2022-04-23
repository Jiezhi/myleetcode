#!/usr/bin/env python
"""
CREATED AT: 2022/4/23
Des:
https://leetcode-cn.com/contest/season/2022-spring/problems/6UEx57/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from math import inf
from typing import List


class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        """
        matrix 中仅包含 '^'、'v'、'<'、'>'
        0 < matrix.length <= 100
        0 < matrix[i].length <= 100
        0 <= start[0],end[0] < matrix.length
        0 <= start[1],end[1] < matrix[i].length
        """
        dq = collections.deque([(start[0], start[1], 0)])
        m, n = len(matrix), len(matrix[0])
        ret = [[inf for _ in range(n)] for _ in range(m)]
        ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while dq:
            x, y, cnt = dq.popleft()
            if not (0 <= x < m and 0 <= y < n):
                continue
            if cnt < ret[x][y]:
                ret[x][y] = cnt
                next_ds = [(x + ds[i][0], y + ds[i][1], cnt + 1) for i in range(4)]
                if matrix[x][y] == '^':
                    next_ds[0] = (next_ds[0][0], next_ds[0][1], cnt)
                elif matrix[x][y] == 'v':
                    next_ds[1] = (next_ds[1][0], next_ds[1][1], cnt)
                elif matrix[x][y] == '<':
                    next_ds[2] = (next_ds[2][0], next_ds[2][1], cnt)
                elif matrix[x][y] == '>':
                    next_ds[3] = (next_ds[3][0], next_ds[3][1], cnt)
                for i in range(4):
                    dq.append(next_ds[i])
        return ret[end[0]][end[1]]


def test():
    assert Solution().conveyorBelt(matrix=[">>v", "v^<", "<><"], start=[0, 1], end=[2, 0]) == 1


if __name__ == '__main__':
    test()
