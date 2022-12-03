#!/usr/bin/env python3
"""
CREATED AT: 2022-12-03

URL: https://leetcode.com/problems/second-largest-digit-in-a-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1796-SecondLargestDigitInAString

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def secondHighest(self, s: str) -> int:
        """
        Runtime: 41 ms, faster than 89.78%
        Memory Usage: 13.8 MB, less than 97.45%
        1 <= s.length <= 500
        s consists of only lowercase English letters and/or digits.
        """
        m1, m2 = -1, -1
        for c in s:
            if c.isdigit():
                n = int(c)
                if n > m1:
                    m1, m2 = n, m1
                elif n != m1 and n > m2:
                    m2 = n
        return m2


def test():
    assert Solution().secondHighest(s="dfa12321afd") == 2
    assert Solution().secondHighest(s="abc1111") == -1


if __name__ == '__main__':
    test()
