#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/power-of-three/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/745/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        21038 / 21038 test cases passed.
        Status: Accepted
        Runtime: 60 ms
        Memory Usage: 14.2 MB
        :param n:
        :return:
        """
        return n > 0 and 1162261467 % n == 0


def test():
    assert Solution().isPowerOfThree(n=27)
    assert not Solution().isPowerOfThree(n=0)
    assert Solution().isPowerOfThree(n=9)
    assert not Solution().isPowerOfThree(n=45)


def get_max_power_three() -> int:
    """
    :return: 1162261467
    """
    i = 0
    m = 2 ** 31 - 1
    while True:
        ret = (3 ** i)
        if ret > m:
            break
        i += 1
    return 3 ** (i - 1)


if __name__ == '__main__':
    # print(get_max_power_three())
    test()
