#!/usr/bin/env python
"""
CREATED AT: 2022/4/5
Des:

https://leetcode.com/problems/longest-word-in-dictionary/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
        Runtime: 138 ms, faster than 67.33%
        Memory Usage: 14.5 MB, less than 55.07%

        1 <= words.length <= 1000
        1 <= words[i].length <= 30
        words[i] consists of lowercase English letters.
        :param words:
        :return:
        """
        ret = ""
        word_set = set(words)
        words = sorted(words, key=lambda x: -len(x))
        for word in words:
            if len(word) < len(ret):
                return ret
            found = True
            for i in range(1, len(word) - 1):
                if word[:-i] not in word_set:
                    found = False
                    break
            if found:
                if len(word) > len(ret):
                    ret = word
                elif word < ret:
                    ret = word
        return ret


def test():
    assert Solution().longestWord(["w", "wo", "wor", "worl", "world"]) == "world"
    assert Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"


if __name__ == '__main__':
    test()
