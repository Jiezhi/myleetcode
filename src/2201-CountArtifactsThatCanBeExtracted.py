#!/usr/bin/env python
"""
CREATED AT: 2022/3/13
Des:

https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        """
        1 <= n <= 1000
        1 <= artifacts.length, dig.length <= min(n2, 10^5)
        artifacts[i].length == 4
        dig[i].length == 2
        0 <= r1i, c1i, r2i, c2i, ri, ci <= n - 1
        r1i <= r2i
        c1i <= c2i
        No two artifacts will overlap.
        The number of cells covered by an artifact is at most 4.
        The entries of dig are unique.
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        for r, c in dig:
            matrix[r][c] = 1

        ret = 0
        for art in artifacts:
            area = 0
            for x in range(art[0], art[2] + 1):
                for y in range(art[1], art[3] + 1):
                    area += matrix[x][y]
            if (art[2] - art[0] + 1) * (art[3] - art[1] + 1) == area:
                ret += 1
        return ret


def test():
    assert Solution().digArtifacts(
        n=2,
        artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]],
        dig=[[0, 0], [0, 1]]) == 1
    assert Solution().digArtifacts(
        n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]],
        dig=[[0, 0], [0, 1], [1, 1]]) == 2


if __name__ == '__main__':
    test()
