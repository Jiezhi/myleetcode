#!/usr/bin/env python
"""
CREATED AT: 2022-06-05
Des: https://leetcode.com/problems/n-queens-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Runtime: 231 ms, faster than 10.72%
        Memory Usage: 13.9 MB, less than 39.44%
        :param n: 1 <= n <= 9
        :return:
        """
        ret = 0
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
                nonlocal ret
                ret += 1
                return
            for i in range(n):
                if (r, i) not in seen:
                    dfs(r + 1, pre + [i], get_seen_set(seen, r, i))

        for i in range(n):
            dfs(1, [i], get_seen_set(set(), 0, i))

        return ret


def test():
    assert Solution().totalNQueens(9) == 352


if __name__ == '__main__':
    test()
