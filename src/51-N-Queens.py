#!/usr/bin/env python
"""
CREATED AT: 2022-06-04
Des: https://leetcode.com/problems/n-queens/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Runtime: 235 ms, faster than 12.16%
        Memory Usage: 14.4 MB, less than 45.52%

        :param n: 1 <= n <= 9
        :return:
        """
        ret = []
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def get_seen_set(pre_seen, x, y):
            seen_set = pre_seen.copy()
            seen_set.add((x, y))
            k = 1
            found = True
            while found:
                found = False
                for dx, dy in dirs:
                    if 0 <= dx * k + x < n and 0 <= dy * k + y < n:
                        found = True
                        seen_set.add((dx * k + x, dy * k + y))
                k += 1
            return seen_set

        def dfs(r, pre, seen):
            if r == n:
                ret.append(['.' * x + 'Q' + '.' * (n - x - 1) for x in pre])
                return
            for i in range(n):
                if (r, i) not in seen:
                    dfs(r + 1, pre + [i], get_seen_set(seen, r, i))

        for i in range(n):
            dfs(1, [i], get_seen_set(set(), 0, i))

        return ret


def test():
    assert Solution().solveNQueens(n=1) == [["Q"]]


if __name__ == '__main__':
    test()
