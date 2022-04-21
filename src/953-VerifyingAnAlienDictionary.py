#!/usr/bin/env python
"""
CREATED AT: 2022/4/21
Des:
https://leetcode.com/problems/verifying-an-alien-dictionary/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Runtime: 53 ms, faster than 43.11%
        Memory Usage: 13.9 MB, less than 42.58%

        1 <= words.length <= 100
        1 <= words[i].length <= 20
        order.length == 26
        All characters in words[i] and order are English lowercase letters.
        """
        d = dict()
        for i, c in enumerate(order):
            d[c] = i

        def compare(a: str, b: str) -> bool:
            diff = False
            for i in range(min(len(a), len(b))):
                if d[a[i]] < d[b[i]]:
                    return True
                if d[a[i]] > d[b[i]]:
                    return False
                elif d[a[i]] != d[b[i]]:
                    diff = True

            return not diff and len(a) <= len(b)

        for i, word in enumerate(words):
            if i == len(words) - 1:
                return True
            if not compare(word, words[i + 1]):
                return False


def test():
    pass


if __name__ == '__main__':
    test()
