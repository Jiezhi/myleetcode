#!/usr/bin/env python3
"""
CREATED AT: 2022-06-30

URL: https://leetcode.com/problems/prime-arrangements/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1175-PrimeArrangements

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        """
        Ref: https://leetcode.com/problems/prime-arrangements/discuss/371862/JavaPython-3-two-codes-each-count-only-primes-then-compute-factorials-for-both-w-analysis.
        Runtime: 52 ms, faster than 37.94% 
        Memory Usage: 13.9 MB, less than 66.40% 
        1 <= n <= 100
        """
        MOD = 10 ** 9 + 7

        primes = [True] * (n + 1)

        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        cnt = sum(primes[2:])
        return math.factorial(cnt) * math.factorial(n - cnt) % MOD


def test():
    assert Solution().numPrimeArrangements(n=5) == 12
    assert Solution().numPrimeArrangements(n=100) == 682289015


if __name__ == '__main__':
    test()
