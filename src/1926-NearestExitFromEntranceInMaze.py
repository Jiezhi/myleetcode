#!/usr/bin/env python3
"""
CREATED AT: 2022-11-21

URL: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan&id=graph-i

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1926-NearestExitFromEntranceInMaze

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Runtime: 968 ms, faster than 82.11%
        Memory Usage: 14.4 MB, less than 86.37%

        maze.length == m
        maze[i].length == n
        1 <= m, n <= 100
        maze[i][j] is either '.' or '+'.
        entrance.length == 2
        0 <= entrancerow < m
        0 <= entrancecol < n
        entrance will always be an empty cell.
        """
        m, n = len(maze), len(maze[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maze[entrance[0]][entrance[1]] = '+'
        dq = deque([(entrance[0], entrance[1], 0)])
        while dq:
            x, y, step = dq.popleft()
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and step != 0:
                return step
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < m or not 0 <= ny < n or maze[nx][ny] == '+':
                    continue
                maze[nx][ny] = '+'
                dq.append((nx, ny, step + 1))
        return -1


def test():
    assert Solution().nearestExit(maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
                                  entrance=[1, 2]) == 1
    assert Solution().nearestExit(maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0]) == 2
    assert Solution().nearestExit(maze=[[".", "+"]], entrance=[0, 0]) == -1


if __name__ == '__main__':
    test()
