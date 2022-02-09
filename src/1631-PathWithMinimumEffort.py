#!/usr/bin/env python
"""
CREATED AT: 2022/2/9
Des:

https://leetcode.com/problems/path-with-minimum-effort/
https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3952/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
import sys
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        CREATED AT: 2022/2/9
        75 / 75 test cases passed.
        Status: Accepted
        Runtime: 7070 ms, faster than
        Memory Usage: 17.1 MB, less than 21.54%
        rows == heights.length
        columns == heights[i].length
        1 <= rows, columns <= 100
        1 <= heights[i][j] <= 10^6
        :param heights:
        :return:
        """
        m, n = len(heights), len(heights[0])
        cost = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        cost[0][0] = 0
        dq = collections.deque()
        dq.append((0, 0))
        visited = set()
        while dq:
            i, j = dq.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i > 0:
                curr_cost = max(abs(heights[i][j] - heights[i - 1][j]), cost[i][j])
                if cost[i - 1][j] > curr_cost:
                    cost[i - 1][j] = curr_cost
                    if (i - 1, j) in visited:
                        visited.remove((i - 1, j))
                dq.append((i - 1, j))
            if j > 0:
                curr_cost = max(abs(heights[i][j] - heights[i][j - 1]), cost[i][j])
                if cost[i][j - 1] > curr_cost:
                    cost[i][j - 1] = curr_cost
                    if (i, j - 1) in visited:
                        visited.remove((i, j - 1))
                dq.append((i, j - 1))
            if i < m - 1:
                curr_cost = max(abs(heights[i][j] - heights[i + 1][j]), cost[i][j])
                if cost[i + 1][j] > curr_cost:
                    cost[i + 1][j] = curr_cost
                    if (i + 1, j) in visited:
                        visited.remove((i + 1, j))
                dq.append((i + 1, j))
            if j < n - 1:
                curr_cost = max(abs(heights[i][j] - heights[i][j + 1]), cost[i][j])
                if cost[i][j + 1] > curr_cost:
                    cost[i][j + 1] = curr_cost
                    if (i, j + 1) in visited:
                        visited.remove((i, j + 1))
                dq.append((i, j + 1))
        return cost[-1][-1]


def test():
    assert Solution().minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert Solution().minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert Solution().minimumEffortPath(
        heights=[[1, 2, 1, 1, 1],
                 [1, 2, 1, 2, 1],
                 [1, 2, 1, 2, 1],
                 [1, 2, 1, 2, 1],
                 [1, 1, 1, 2, 1]]) == 0


if __name__ == '__main__':
    test()
