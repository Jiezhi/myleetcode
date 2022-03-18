#!/usr/bin/env python
"""
CREATED AT: 2022/3/18
Des:
https://leetcode.com/problems/maximum-number-of-words-you-can-type/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Runtime: 51 ms, faster than 39.05%
        Memory Usage: 14.1 MB, less than 45.58%

        1 <= text.length <= 10^4
        0 <= brokenLetters.length <= 26
        text consists of words separated by a single space without any leading or trailing spaces.
        Each word only consists of lowercase English letters.
        brokenLetters consists of distinct lowercase English letters.
        """
        if len(brokenLetters) == 26:
            return 0
        words = text.split(' ')
        if len(brokenLetters) == 0:
            return len(words)
        ret = 0
        broken = set(brokenLetters)
        for word in words:
            if any(c in broken for c in word):
                continue
            ret += 1
        return ret


def test():
    assert Solution().canBeTypedWords(text="hello world", brokenLetters="ad") == 1
    assert Solution().canBeTypedWords(text="leet code", brokenLetters="e") == 0


if __name__ == '__main__':
    test()
