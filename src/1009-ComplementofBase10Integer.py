#!/usr/bin/env python
"""
CREATED AT: 2022/1/4
Des:

https://leetcode.com/problems/complement-of-base-10-integer/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: Bit

See: 

Time Spent:  min
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        Runtime: 43 ms, faster than 9.05%
        Memory Usage: 14.3 MB, less than 38.43%
        0 <= n < 10^9
        :param n:
        :return:
        """
        ret = []
        n_str = format(n, 'b')
        for c in n_str:
            if c == '1':
                ret.append('0')
            else:
                ret.append('1')
        return int(''.join(ret), 2)


def test():
    assert Solution().bitwiseComplement(n=5) == 2
    assert Solution().bitwiseComplement(n=7) == 0
    assert Solution().bitwiseComplement(n=10) == 5


if __name__ == '__main__':
    test()
