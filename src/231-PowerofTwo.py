#!/usr/bin/env python
"""
CREATED AT: 2021/10/3
Des:
https://leetcode.com/problems/power-of-two/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""


class Solution:
    def isPowerOfTwo2(self, n: int) -> bool:
        """
        Update: 2021/12/21
        Notes: 用一条语句判断一个整数是不是2的整数次方。一个整数如果是2的整数次方，那么它的二进制表示中有且只有一位是1，而其他所有位都是0。
        把这个整数减去1之后再和它自己做与运算，这个整数中唯一的1就会变成0。

        Runtime: 24 ms, faster than 96.97%
        Memory Usage: 14.1 MB, less than 89.51%
        :param n: -2^31 <= n <= 2^31 - 1
        :return:
        """
        if n <= 0:
            return False
        return n & (n - 1) == 0

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
    assert Solution().isPowerOfTwo2(n=1)
    assert Solution().isPowerOfTwo2(n=16)
    assert not Solution().isPowerOfTwo2(n=3)

    assert Solution().isPowerOfTwo(n=1)
    assert Solution().isPowerOfTwo(n=16)
    assert not Solution().isPowerOfTwo(n=3)


if __name__ == '__main__':
    test()
