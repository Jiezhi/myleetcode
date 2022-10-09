#!/usr/bin/env python3
"""
CREATED AT: 2022-10-09

URL: https://leetcode.com/contest/weekly-contest-314/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2435-PathsInMatrixWhoseSumIsDivisibleByK

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7

        def merge(d1, d2, num):
            ret = {x: 0 for x in range(k)}
            for key, value in d1.items():
                ret[(key + num) % k] += value
                ret[(key + num) % k] %= mod
            for key, value in d2.items():
                ret[(key + num) % k] += value
                ret[(key + num) % k] %= mod
            return ret

        @cache
        def get_path_sum(x, y):
            if not 0 <= x < m or not 0 <= y < n:
                return {}
            if x == m - 1 and y == n - 1:
                return {grid[x][y] % k: 1}
            return merge(get_path_sum(x + 1, y), get_path_sum(x, y + 1), grid[x][y])

        cnt = get_path_sum(0, 0)
        return 0 if 0 not in cnt else cnt[0]


def test():
    assert Solution().numberOfPaths(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3) == 2
    assert Solution().numberOfPaths(grid=[[0, 0]], k=5) == 1
    assert Solution().numberOfPaths(grid=[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k=1) == 10


if __name__ == '__main__':
    test()
