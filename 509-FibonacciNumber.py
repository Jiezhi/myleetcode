#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-08-13

Leetcode: https://leetcode.com/problems/fibonacci-number

"""


class Solution:
    cache = {}

    def fib(self, N: int) -> int:
        if N < 2:
            return N
        if N in self.cache:
            return self.cache[N]
        else:
            ret = self.fib(N - 1) + self.fib(N - 2)
            self.cache[N] = ret
            return ret


def test():
    assert Solution().fib(0) == 0
    assert Solution().fib(1) == 1
    assert Solution().fib(2) == 1
    assert Solution().fib(4) == 3


if __name__ == '__main__':
    test()
