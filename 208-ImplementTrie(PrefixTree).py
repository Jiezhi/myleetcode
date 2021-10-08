#!/usr/bin/env python
"""
CREATED AT: 2021/10/08
Des:
https://leetcode.com/problems/implement-trie-prefix-tree/
https://leetcode.com/explore/learn/card/trie/147/basic-operations/1047/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/explore/learn/card/trie/150/introduction-to-trie/1045/

Difficulty: Medium
"""


class Trie:
    """
    15 / 15 test cases passed.
    Status: Accepted
    Runtime: 120 ms
    Memory Usage: 27.9 MB

    Reference other people answers
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


def test():
    trie = Trie()
    trie.insert('apple')
    assert trie.search('apple')
    assert not trie.search('app')
    assert trie.startsWith('app')
    trie.insert("app")
    assert trie.search('app')


if __name__ == '__main__':
    test()
