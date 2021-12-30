#!/usr/bin/env python
"""
CREATED AT: 2021/12/30
Des:

https://leetcode.com/problems/smallest-integer-divisible-by-k/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: https://leetcode.com/problems/smallest-integer-divisible-by-k/solution/

Note:
    1. Since the remainder and N have the same remainder of K, it OK to use remainder instead of N.

Time Spent:  min
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Note: the last num to be 1 means the last num of k must be one of 1, 3, 7, 9

        Runtime: 84 ms, faster than 27.03%
        Memory Usage: 14.3 MB, less than 65.77%

        1 <= k <= 10^5
        :param k:
        :return:
        """
        if k % 10 not in [1, 3, 7, 9]:
            return -1
        remainder = 0
        for length_N in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length_N

    def smallestRepunitDivByK2(self, k: int) -> int:
        """
        Note: the last num to be 1 means the last num of k must be one of 1, 3, 7, 9

        Runtime: 2621 ms, faster than 5.41%
        Memory Usage: 14.4 MB, less than 40.54%
        1 <= k <= 10^5
        :param k:
        :return:
        """
        if k % 10 not in [1, 3, 7, 9]:
            return -1
        ret = 0
        tmp = 0
        while True:
            tmp = tmp * 10 + 1
            if tmp % k == 0:
                return ret + 1
            ret += 1


def test():
    assert Solution().smallestRepunitDivByK(k=1) == 1
    assert Solution().smallestRepunitDivByK(k=2) == -1
    assert Solution().smallestRepunitDivByK(k=3) == 3
    assert Solution().smallestRepunitDivByK(k=7) == 6
    assert Solution().smallestRepunitDivByK(k=9) == 9
    assert Solution().smallestRepunitDivByK(k=11) == 2
    assert Solution().smallestRepunitDivByK(k=13) == 6


if __name__ == '__main__':
    test()
