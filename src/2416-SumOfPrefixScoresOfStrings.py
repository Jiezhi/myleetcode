#!/usr/bin/env python3
"""
CREATED AT: 2022-09-18

URL: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2416-SumOfPrefixScoresOfStrings

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {'*': 1}
            else:
                cur[c]['*'] += 1
            cur = cur[c]
        cur['#'] = True

    def get_cnt(self, word):
        cur = self.root
        ret = 0
        for c in word:
            ret += cur[c]['*']
            cur = cur[c]
        return ret


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        return [trie.get_cnt(word) for word in words]


def test():
    assert Solution().sumPrefixScores(words=["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]
    assert Solution().sumPrefixScores(words=["abcd"]) == [4]


if __name__ == '__main__':
    test()
