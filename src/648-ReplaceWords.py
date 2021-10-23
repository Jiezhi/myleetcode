#!/usr/bin/env python
"""
CREATED AT: 2021/10/8
Des:
https://leetcode.com/problems/replace-words/
https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1053/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

See: 208

Tag: Trie
"""
from typing import List


# See: 208
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def get_word_root(self, word):
        cur = self.root
        ret = ''
        for c in word:
            if c not in cur:
                return word
            ret += c
            cur = cur[c]
            if '#' in cur:
                return ret
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        126 / 126 test cases passed.
        Status: Accepted
        Runtime: 68 ms
        Memory Usage: 28.3 MB
        :param dictionary:
        :param sentence:
        :return:
        """
        trie = Trie()
        [trie.insert(x) for x in dictionary]
        ret = [trie.get_word_root(x) for x in sentence.split()]
        return ' '.join(ret)


def test():
    assert Solution().replaceWords(
        dictionary=["a", "aa", "aaa", "aaaa"],
        sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    ) == "a a a a a a a a bbb baba a"

    assert Solution().replaceWords(
        dictionary=["cat", "bat", "rat"],
        sentence="the cattle was rattled by the battery"
    ) == "the cat was rat by the bat"


if __name__ == '__main__':
    test()
