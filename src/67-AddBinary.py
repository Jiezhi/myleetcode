#!/usr/bin/env python
"""
https://leetcode.com/problems/add-binary/

Created on 2018-11-15
Updated on 2022-01-10

@author: 'Jiezhi.G@gmail.com'

Make a/b to a int, then add them and turn the result to binary format

Reference: 
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Updated on 2022-01-10 for daily quest.
        Runtime: 46 ms, faster than 22.02%
        Memory Usage: 14.4 MB, less than 22.51%

        1 <= a.length, b.length <= 10^4
        a and b consist only of '0' or '1' characters.
        Each string does not contain leading zeros except for the zero itself.
        :param a:
        :param b:
        :return:
        """
        # make sure a is the longer
        if len(a) < len(b):
            a, b = b, a
        ret = [0] * len(a)
        carry = 0
        i = 1
        while i < len(b) + 1:
            carry, ret[-i] = divmod(int(a[-i]) + int(b[-i]) + carry, 2)
            i += 1
        while carry and i < len(a) + 1:
            carry, ret[-i] = divmod(int(a[-i]) + carry, 2)
            i += 1
        if carry:
            # all num in a were processed
            return '1' + ''.join(str(x) for x in ret)
        else:
            # now i == len(a) + 1
            return a[:-i + 1] + ''.join(str(x) for x in ret[-i + 1:])

    def addBinary2(self, a, b):
        """
        Runtime: 32 ms, faster than 80.60%
        Memory Usage: 14.3 MB, less than 22.51%

        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')


def test():
    assert Solution().addBinary("1", "111") == "1000"
    assert Solution().addBinary("111", "1") == "1000"
    assert Solution().addBinary("11", "11") == "110"
    assert Solution().addBinary("1010", "1011") == "10101"

    assert Solution().addBinary2("1", "111") == "1000"
    assert Solution().addBinary2("111", "1") == "1000"
    assert Solution().addBinary2("11", "11") == "110"
    assert Solution().addBinary2("1010", "1011") == "10101"

    assert Solution().addBinary("1010111111111", "1011") == Solution().addBinary2("1010111111111", "1011")


if __name__ == '__main__':
    test()
