#!/usr/bin/env python3
"""
CREATED AT: 2022-10-16

URL: https://leetcode.com/problems/range-product-queries-of-powers/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2438-RangeProductQueriesOfPowers

Difficulty: 

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
                  524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728,
                  268435456, 536870912, 1073741824]
        p = []
        while n > 0:
            pos = bisect.bisect_left(powers, n)
            if powers[pos] == n:
                p.append(pos)
                break
            p.append(pos - 1)
            n -= powers[pos - 1]
        p = p[::-1]
        ret = []
        for l, r in queries:
            ret.append((2 ** sum(p[l: r + 1])) % mod)
        return ret


def test():
    assert Solution().productQueries(n=15, queries=[[0, 1], [2, 2], [0, 3]]) == [2, 4, 64]


if __name__ == '__main__':
    test()
