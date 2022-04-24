#!/usr/bin/env python
"""
CREATED AT: 2022/4/24
Des:
https://leetcode.com/problems/binary-gap/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Runtime: 48 ms, faster than 39.42%
        Memory Usage: 13.8 MB, less than 96.88%

        1 <= n <= 10^9
        """
        if n & (n - 1) == 0:
            return 0
        ret = 0
        pre = -1
        pos = 0
        while n > 0:
            if n & 1 == 1:
                if pre == -1:
                    pre = pos
                else:
                    ret = max(ret, pos - pre)
                    pre = pos
            n >>= 1
            pos += 1
        return ret


def test():
    assert Solution().binaryGap(22) == 2
    assert Solution().binaryGap(5) == 2


if __name__ == '__main__':
    test()
