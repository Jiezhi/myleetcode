#!/usr/bin/env python
"""
CREATED AT: 2022/4/27
Des:
https://leetcode.com/problems/search-suggestions-system/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 79, 211

"""
import string
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
        cur['#'] = True

    def suggest(self, word: str) -> List[str]:
        cur = self.root
        for c in word:
            if c not in cur:
                return []
            cur = cur[c]
        ret = []

        def dfs(pre, level):
            nonlocal ret
            if len(ret) >= 3:
                return
            if '#' in level:
                ret.append(pre)
            for c in string.ascii_lowercase:
                if c in level:
                    dfs(pre + c, level[c])

        dfs(word, cur)
        return ret


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        41 / 41 test cases passed.
        Runtime: 1273 ms, faster than 9.85%
        Memory Usage: 21.6 MB, less than 16.88%
        1 <= products.length <= 1000
        1 <= products[i].length <= 3000
        1 <= sum(products[i].length) <= 2 * 10^4
        All the strings of products are unique.
        products[i] consists of lowercase English letters.
        1 <= searchWord.length <= 1000
        searchWord consists of lowercase English letters.
        """
        trie = Trie()

        for p in products:
            trie.add(p)

        return [trie.suggest(searchWord[:i]) for i in range(1, len(searchWord) + 1)]


def test():
    assert Solution().suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse") == [
               ["mobile", "moneypot", "monitor"],
               ["mobile", "moneypot", "monitor"],
               ["mouse", "mousepad"],
               ["mouse", "mousepad"],
               ["mouse", "mousepad"]
           ]


if __name__ == '__main__':
    test()
