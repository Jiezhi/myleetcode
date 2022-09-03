#!/usr/bin/env python3
"""
CREATED AT: 2022-09-03

URL: https://leetcode.com/problems/numbers-with-same-consecutive-differences/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 967-NumbersWithSameConsecutiveDifferences

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """
        Runtime: 112 ms, faster than 5.10%
        Memory Usage: 14 MB, less than 93.88%

        2 <= n <= 9
        0 <= k <= 9
        """
        if k == 0:
            s = 0
            for j in range(n):
                s += 1 * 10 ** (n - j - 1)
            return [s * i for i in range(1, 10)]
        ret = []
        for i in range(1, 10):
            stack = [([i] * n, 1)]
            while stack:
                num, pos = stack.pop()
                if pos == n:
                    s = 0
                    for j in range(n):
                        s += num[j] * 10 ** (n - j - 1)
                    ret.append(s)
                    continue
                num_copy = num.copy()
                num_copy[pos] = num[pos - 1] + k
                if num_copy[pos] < 10:
                    stack.append((num_copy, pos + 1))
                num_copy = num.copy()
                num_copy[pos] = num[pos - 1] - k
                if num_copy[pos] >= 0:
                    stack.append((num_copy, pos + 1))
        return ret


def test():
    assert Solution().numsSameConsecDiff(n=3, k=7) == [181, 292, 707, 818, 929]
    assert Solution().numsSameConsecDiff(n=2, k=0) == [11, 22, 33, 44, 55, 66, 77, 88, 99]
    assert Solution().numsSameConsecDiff(n=2, k=1) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89,
                                                       98]


if __name__ == '__main__':
    test()
