#!/usr/bin/env python
"""
CREATED AT: 2021/10/9
Des: Keep this for backup

https://leetcode.com/problems/word-search-ii/
https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1056/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tags: Trie

See: 208, 79
"""
import copy
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


def get_sub_seq(x, y, board, cur_depth, max_depth=10) -> set:
    if cur_depth >= max_depth:
        return set()
    cur_depth += 1
    c = board[x][y]
    board[x][y] = '0'
    if c == '0':
        return set()
    ret = [c]
    if board[x][y - 1] != '0':
        ret += [c + x for x in get_sub_seq(x, y - 1, copy.deepcopy(board), cur_depth, max_depth)]
    if board[x][y + 1] != '0':
        ret += [c + x for x in get_sub_seq(x, y + 1, copy.deepcopy(board), cur_depth, max_depth)]
    if board[x - 1][y] != '0':
        ret += [c + x for x in get_sub_seq(x - 1, y, copy.deepcopy(board), cur_depth, max_depth)]
    if board[x + 1][y] != '0':
        ret += [c + x for x in get_sub_seq(x + 1, y, copy.deepcopy(board), cur_depth, max_depth)]
    # four directions are '0', just return the last one

    return set(ret)


class Solution:

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
        m, n = len(board), len(board[0])

        board2 = [['0' for _ in range(n + 2)] for _ in range(m + 2)]
        m, n = len(board2), len(board2[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                board2[i][j] = board[i - 1][j - 1]
        max_length = 0
        for w in words:
            max_length = max(max_length, len(w))

        board_words = set()
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                ret = get_sub_seq(i, j, copy.deepcopy(board2), cur_depth=0, max_depth=max_length)
                board_words = board_words.union(ret)

        trie = Trie()
        for bw in board_words:
            trie.insert(bw)
        ret = []
        for word in words:
            if trie.startsWith(word):
                ret.append(word)
        return ret


def test():
    assert tool.equal_list_value(Solution().findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]), ["eat", "oath"])

    assert Solution().findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]) == []

    # ret = Solution().findWords([["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #                             ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]],
    #                            ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa",
    #                             "aaaaaaaaaa"])
    #
    # print(ret)


if __name__ == '__main__':
    test()
