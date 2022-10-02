#!/usr/bin/env python3
"""
CREATED AT: 2022-10-02

URL: https://leetcode.com/problems/minimize-xor/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2429-MinimizeXOR

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        1 <= num1, num2 <= 10^9
        """
        n1, n2 = num1.bit_count(), num2.bit_count()
        if n1 == n2:
            return num1
        elif n1 > n2:
            ret, diff = num1, n1 - n2
            for i in range(num1.bit_length()):
                if (num1 >> i) & 1:
                    ret ^= 1 << i
                    diff -= 1
                    if diff == 0:
                        return ret
        else:
            diff = n2 - n1
            ret = num1
            for i in range(num1.bit_length()):
                if (num1 >> i) & 1 == 0:
                    ret ^= 1 << i
                    diff -= 1
                    if diff == 0:
                        return ret
            i = num1.bit_length()
            while diff > 0:
                diff -= 1
                ret ^= 1 << i
                i += 1
            return ret


def test():
    assert Solution().minimizeXor(num1=3, num2=5) == 3
    assert Solution().minimizeXor(num1=1, num2=12) == 3


if __name__ == '__main__':
    test()
