#!/usr/bin/env python3
"""
CREATED AT: 2022-09-24

URL: https://leetcode.com/problems/defuse-the-bomb/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1652-DefuseTheBomb

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Runtime: 43 ms, faster than 92.75%
        Memory Usage: 13.9 MB, less than 25.91%

        n == code.length
        1 <= n <= 100
        1 <= code[i] <= 100
        -(n - 1) <= k <= n - 1
        """
        n = len(code)
        if k == 0:
            return [0] * n
        ret = []
        if k > 0:
            s = sum(code[:k])
            for i in range(n):
                s += code[(i + k) % n] - code[i]
                ret.append(s)
            return ret
        else:
            s = sum(code[k:])
            for i in range(n):
                ret.append(s)
                s += code[i] - code[(i + k) % n]
            return ret


def test():
    assert Solution().decrypt(code=[5, 7, 1, 4], k=3) == [12, 10, 16, 13]
    assert Solution().decrypt(code=[1, 2, 3, 4], k=0) == [0, 0, 0, 0]
    assert Solution().decrypt(code=[2, 4, 9, 3], k=-2) == [12, 5, 6, 13]
    assert Solution().decrypt(code=[10, 5, 7, 7, 3, 2, 10, 3, 6, 9, 1, 6], k=-4) == [22, 26, 22, 28, 29, 22, 19, 22, 18,
                                                                                     21, 28, 19]


if __name__ == '__main__':
    test()
