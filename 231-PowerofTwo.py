#!/usr/bin/env python
"""
CREATED AT: 2021/10/3
Des:
https://leetcode.com/problems/power-of-two/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        1108 / 1108 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.2 MB
        :param n:
        :return:
        """
        return n in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
                     524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
                     536870912, 1073741824, 2147483648]


def test():
    assert Solution().isPowerOfTwo(n=1)
    assert Solution().isPowerOfTwo(n=16)
    assert not Solution().isPowerOfTwo(n=3)


if __name__ == '__main__':
    test()
