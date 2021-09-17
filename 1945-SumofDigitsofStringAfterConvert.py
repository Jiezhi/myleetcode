#!/usr/bin/env python
"""
CREATED AT: 2021/7/25
Des:

https://leetcode.com/problems/sum-of-digits-of-string-after-convert
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1 = ''
        for c in s:
            s1 += str(ord(c) - 96)
        for i in range(k):
            s1 = str(sum([int(x) for x in s1]))
        return int(s1)


def test():
    assert Solution().getLucky("zbax", 2) == 8
    assert Solution().getLucky("leetcode", 2) == 6
    assert Solution().getLucky("iiii", 1) == 36
    assert Solution().getLucky("hvmhoasabaymnmsd", 1) == 79


if __name__ == '__main__':
    test()
