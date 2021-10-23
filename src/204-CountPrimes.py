#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/count-primes/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/744/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from math import sqrt, ceil

from tool import print_results


class Solution:
    @print_results
    def countPrimes(self, n: int) -> int:
        """
        21 / 21 test cases passed.
        Status: Accepted
        Runtime: 5728 ms
        Memory Usage: 67.9 MB
        :param n:
        :return:
        """
        if n <= 1:
            return 0
        primes = [1 for _ in range(n)]
        primes[0] = 0
        primes[1] = 0
        n_sqrt = ceil(sqrt(n))
        for i in range(2, n_sqrt):
            j = i * i
            while j < n:
                primes[j] = 0
                j += i
        return sum(primes)


def test():
    assert Solution().countPrimes(n=100) == 25
    assert Solution().countPrimes(n=0) == 0
    assert Solution().countPrimes(n=1) == 0


if __name__ == '__main__':
    test()
