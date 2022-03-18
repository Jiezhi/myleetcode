#!/usr/bin/env python
"""
CREATED AT: 2022/3/18
Des:

https://leetcode.com/problems/reverse-prefix-of-word/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Runtime: 24 ms, faster than 98.50%
        Memory Usage: 13.9 MB, less than 32.10%

        1 <= word.length <= 250
        word consists of lowercase English letters.
        ch is a lowercase English letter.
        """
        pos = None
        for i in range(len(word)):
            if word[i] == ch:
                pos = i
                break
        if not pos:
            return word

        return word[0:pos + 1][::-1] + word[pos + 1:]


def test():
    assert Solution().reversePrefix("abca", "a") == "abca"
    assert Solution().reversePrefix("abca", "b") == "baca"


if __name__ == '__main__':
    test()
