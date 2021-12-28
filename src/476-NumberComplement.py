#!/usr/bin/env python
"""
CREATED AT: 2021/12/27
Des:

https://leetcode.com/problems/number-complement/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: Bit

See: 1009

Time Spent:  min

Ref: https://leetcode.com/problems/number-complement/discuss/95992/Java-1-line-bit-manipulation-solution
https://leetcode.com/problems/number-complement/discuss/96026/Python-4-ways

Notes:
    1. turn int num to binary str with/without leading '0b'
    >>> format(14, '#b'), format(14, 'b')
    ('0b1110', '1110')
    2. turn binary string to int (base 10)
    >>> int('1110', 2)
    3. get the number of bits necessary to represent an integer in binary,
     excluding the sign and leading zeros
    >>> int.bit_length()
"""


class Solution:
    def findComplement2(self, num: int) -> int:
        """
        Runtime: 32 ms, faster than 55.58%
        Memory Usage: 14 MB, less than 97.18%
        1 <= num < 2^31
        :param num:
        :return:
        """
        return ~num & ((1 << num.bit_length()) - 1)

    def findComplement(self, num: int) -> int:
        """
        Runtime: 28 ms, faster than 81.72%
        Memory Usage: 14.3 MB, less than 7.36%
        1 <= num < 2^31
        :param num:
        :return:
        """
        num_str = format(num, 'b')
        ret = ''
        for b in num_str:
            if b == '1':
                ret += '0'
            else:
                ret += '1'
        return int(ret, 2)


def test():
    assert Solution().findComplement(num=5) == 2
    assert Solution().findComplement(num=4) == 3
    assert Solution().findComplement(num=1) == 0

    assert Solution().findComplement2(num=4) == 3
    assert Solution().findComplement2(num=5) == 2
    assert Solution().findComplement2(num=1) == 0


if __name__ == '__main__':
    test()
