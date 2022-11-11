#!/usr/bin/env python3
"""
CREATED AT: 2022-11-11

URL: https://leetcode.com/problems/determine-if-string-halves-are-alike/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1704-DetermineIfStringHalvesAreAlike

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Runtime: 69 ms, faster than 47.32%
        Memory Usage: 14 MB, less than 31.65%

        2 <= s.length <= 1000
        s.length is even.
        s consists of uppercase and lowercase letters.
        """
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a, b = 0, 0
        for i in range(n // 2):
            if s[i] in vowels:
                a += 1
            if s[-i - 1] in vowels:
                b += 1
        return a == b


def test():
    assert Solution().halvesAreAlike(s="book")
    assert not Solution().halvesAreAlike(s="textbook")


if __name__ == '__main__':
    test()
