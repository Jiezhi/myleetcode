#!/usr/bin/env python
"""
CREATED AT: 2022/4/29
Des:
https://leetcode.com/problems/construct-quad-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        Runtime: 276 ms, faster than 6.29%
        Memory Usage: 14.8 MB, less than 66.17%
        n == grid.length == grid[i].length
        n == 2^x where 0 <= x <= 6
        """
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True, None, None, None, None)
        tl = self.construct([[grid[x][y] for y in range(n // 2)] for x in range(n // 2)])
        tr = self.construct([[grid[x][y] for y in range(n // 2, n)] for x in range(n // 2)])
        bl = self.construct([[grid[x][y] for y in range(n // 2)] for x in range(n // 2, n)])
        br = self.construct([[grid[x][y] for y in range(n // 2, n)] for x in range(n // 2, n)])
        children = [tl, tr, bl, br]
        if all(x.isLeaf for x in children):
            s = sum(x.val for x in children)
            if s == 0:
                return Node(0, True, None, None, None, None)
            elif s == 4:
                return Node(1, True, None, None, None, None)
        return Node(1, False, tl, tr, bl, br)


def test():
    Solution().construct(grid=[[0, 1], [1, 0]])


if __name__ == '__main__':
    test()
