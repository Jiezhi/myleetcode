#!/usr/bin/env python3
"""
CREATED AT: 2022-08-01

URL: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1374-GenerateAStringWithCharactersThatHaveOddCounts

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def generateTheString(self, n: int) -> str:
        """
        Runtime: 32 ms, faster than 91.45%
        Memory Usage: 13.7 MB, less than 95.80%

        1 <= n <= 500
        """
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        else:
            return 'a' * n


def test():
    assert Solution().generateTheString(n=4) == "aaab"
    assert Solution().generateTheString(n=2) == "ab"
    assert Solution().generateTheString(n=7) == "aaaaaaa"


if __name__ == '__main__':
    test()
