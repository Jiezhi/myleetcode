#!/usr/bin/env python
"""
CREATED AT: 2021/10/9
Des:

https://leetcode.com/problems/word-search-ii/
https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1056/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).

Difficulty: Hard

Tags: Trie

See: 208, 79
"""
from typing import List

import tool


class Trie:
    """
    Copied from 208
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


class Solution:
    """
    51 / 51 test cases passed.
    Status: Accepted
    Runtime: 4528 ms
    Memory Usage: 14.6 MB
    """

    def dfs(self, x, y, board, cur, ret, path):
        if '#' in cur and cur['#']:
            ret.append(path)
            cur['#'] = False
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == '#':
            return
        tmp = board[x][y]
        if tmp not in cur:
            return
        cur = cur[tmp]
        board[x][y] = '#'
        self.dfs(x, y - 1, board, cur, ret, path + tmp)
        self.dfs(x, y + 1, board, cur, ret, path + tmp)
        self.dfs(x - 1, y, board, cur, ret, path + tmp)
        self.dfs(x + 1, y, board, cur, ret, path + tmp)
        board[x][y] = tmp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 12
        board[i][j] is a lowercase English letter.
        1 <= words.length <= 3 * 104
        1 <= words[i].length <= 10
        words[i] consists of lowercase English letters.
        All the strings of words are unique.
        :param board:
        :param words:
        :return:
        """
        trie = Trie()
        ret = []
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                cur = trie.root
                if len(ret) == len(words):
                    return ret
                self.dfs(i, j, board, cur, ret, "")
        return ret


def test():
    assert tool.equal_list_value(Solution().findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]), ["eat", "oath"])

    assert Solution().findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]) == []

    assert tool.equal_list_value(Solution().findWords(
        [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]],
        words=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
               "aaaaaaaa",
               "aaaaaaaaa",
               "aaaaaaaaaa"]),
        ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa',
         'aaaaaaaaaa']
    )


if __name__ == '__main__':
    test()
