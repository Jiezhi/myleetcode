#!/usr/bin/env python3
"""
CREATED AT: 2022-07-18

URL: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 363-MaxSumOfRectangleNoLargerThanK

Difficulty: Hard

Desc: 

Tag: 

See: 560, 1074

"""
import bisect
from math import inf
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Runtime: 3324 ms, faster than 63.82%
        Memory Usage: 14.7 MB, less than 95.22%

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 100
        -100 <= matrix[i][j] <= 100
        -10^5 <= k <= 10^5
        """
        m, n = len(matrix), len(matrix[0])
        ret = -inf
        for i in range(m):
            acc = [0] * n
            for j in range(i, m):
                for x in range(n):
                    acc[x] += matrix[j][x]
                sorted_acc = [0]
                pre = 0
                for num in acc:
                    pre += num
                    pos = bisect.bisect_left(sorted_acc, pre - k)
                    if pos < len(sorted_acc):
                        if sorted_acc[pos] == pre - k:
                            return k
                        ret = max(ret, pre - sorted_acc[pos])
                    pos = bisect.bisect(sorted_acc, pre)
                    if pos == len(sorted_acc):
                        sorted_acc.append(pre)
                    elif sorted_acc[pos] != pre:
                        sorted_acc.insert(pos, pre)

        return ret


def test():
    assert Solution().maxSumSubmatrix(matrix=[[1, 0, 1], [0, -2, 3]], k=2) == 2
    assert Solution().maxSumSubmatrix(matrix=[[2, 2, -1]], k=2) == 2
    assert Solution().maxSumSubmatrix(matrix=[[2, 2, -1]], k=3) == 3
    assert Solution().maxSumSubmatrix(matrix=[[2, 2, -1]], k=0) == -1
    assert Solution().maxSumSubmatrix(matrix=[list(range(100)) for _ in range(100)], k=5555555) == 495000


if __name__ == '__main__':
    test()
