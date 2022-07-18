#!/usr/bin/env python3
"""
CREATED AT: 2022-07-18

URL: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1074-NumberOfSubmatricesThatSumToTarget

Difficulty: Hard

Desc: 

Tag: 

See: 560

"""
import collections
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Ref: https://leetcode.cn/problems/number-of-submatrices-that-sum-to-target/solution/yuan-su-he-wei-mu-biao-zhi-de-zi-ju-zhen-8ym2/
        Runtime: 1661 ms, faster than 31.28%
        Memory Usage: 14.9 MB, less than 47.39%
        1 <= matrix.length <= 100
        1 <= matrix[0].length <= 100
        -1000 <= matrix[i] <= 1000
        -10^8 <= target <= 10^8
        """
        m, n = len(matrix), len(matrix[0])
        ret = 0

        for i in range(m):
            acc = [0] * n
            for j in range(i, m):
                for x in range(n):
                    acc[x] += matrix[j][x]
                cnt = collections.Counter([0])
                pre = 0
                for num in acc:
                    pre += num
                    ret += cnt[pre - target]
                    cnt[pre] += 1

        return ret


def test():
    assert Solution().numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0) == 4
    assert Solution().numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0) == 5
    assert Solution().numSubmatrixSumTarget(matrix=[[904]], target=0) == 0
    assert Solution().numSubmatrixSumTarget(matrix=[list(range(100)) * 100], target=0) == 100


if __name__ == '__main__':
    test()
