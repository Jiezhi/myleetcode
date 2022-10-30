#!/usr/bin/env python3
"""
CREATED AT: 2022-10-30

URL: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1293-ShortestPathInAGridWithObstaclesElimination

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        Ref: https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/solution/wang-ge-zhong-de-zui-duan-lu-jing-by-leetcode-solu/
        Runtime: 83 ms, faster than 94.55%
        Memory Usage: 15.5 MB, less than 66.91%
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 40
        1 <= k <= m * n
        grid[i][j] is either 0 or 1.
        grid[0][0] == grid[m - 1][n - 1] == 0
        """
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2 or (m == 1 and n == 1):
            return m + n - 2
        k = min(k, m + n - 3)

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dq = deque([(0, 0, k, 1)])

        seen = {(0, 0, k)}

        while dq:
            x, y, k, cnt = dq.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0 and (nx, ny, k) not in seen:
                        if nx == m - 1 and ny == n - 1:
                            return cnt
                        seen.add((nx, ny, k))
                        dq.append((nx, ny, k, cnt + 1))
                    elif grid[nx][ny] == 1 and k > 0 and (nx, ny, k - 1) not in seen:
                        seen.add((nx, ny, k - 1))
                        dq.append((nx, ny, k - 1, cnt + 1))

        return -1


def test():
    assert Solution().shortestPath(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1) == 6
    assert Solution().shortestPath(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1) == -1


if __name__ == '__main__':
    test()
