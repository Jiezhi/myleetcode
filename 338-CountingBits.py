#!/usr/bin/env python
"""
CREATED AT: 2021/10/10
Des:

https://leetcode.com/problems/counting-bits/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import List

from tool import print_results


class Solution:
    @print_results
    def countBits(self, n: int) -> List[int]:
        """
        Runtime: 68 ms, faster than 99.21% of Python3 online submissions for Counting Bits.
        Memory Usage: 20.8 MB, less than 90.67% of Python3 online submissions for Counting Bits.
        :param n:
        :return:
        """
        ret = [0, 1, 1, 2]
        i = 2
        while 2 ** i <= n:
            ret += [x + 1 for x in ret]
            i += 1
        return ret[:n + 1]


def test():
    assert Solution().countBits(n=2) == [0, 1, 1]
    assert Solution().countBits(n=3) == [0, 1, 1, 2]
    assert Solution().countBits(n=4) == [0, 1, 1, 2, 1]
    assert Solution().countBits(n=5) == [0, 1, 1, 2, 1, 2]

    Solution().countBits(n=10 ** 5)


if __name__ == '__main__':
    test()
