#!/usr/bin/env python3
"""
CREATED AT: 2022-06-20

URL: https://leetcode.com/problems/short-encoding-of-words/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 820-ShortEncodingOfWords

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

    def getEncodingLength(self) -> int:
        ret = 0
        stack = [(self.root, 1)]
        while stack:
            cur, cnt = stack.pop()
            print(cur)
            if not cur:
                ret += cnt
            else:
                for c in cur.keys():
                    stack.append((cur[c], cnt + 1))
        return ret


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        Runtime: 213 ms, faster than 69.30%
        Memory Usage: 15.9 MB, less than 59.53%

        1 <= words.length <= 2000
        1 <= words[i].length <= 7
        words[i] consists of only lowercase letters.
        """
        trie = Trie()

        for word in words:
            trie.add(word[::-1])

        return trie.getEncodingLength()


def test():
    assert Solution().minimumLengthEncoding(words=["time", "me", "bell"]) == 10
    assert Solution().minimumLengthEncoding(words=["t"]) == 2


if __name__ == '__main__':
    test()
