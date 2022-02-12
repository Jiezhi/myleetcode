#!/usr/bin/env python
"""
CREATED AT: 2022/1/5
Des:

https://leetcode.com/problems/word-ladder/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

Time Spent:  min
"""
import collections
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        CREATED AT: 2022/2/12
        Runtime: 591 ms, faster than 31.96%
        Memory Usage: 15.1 MB, less than 90.62%
        1 <= beginWord.length <= 10
        endWord.length == beginWord.length
        1 <= wordList.length <= 5000
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        dq = collections.deque()

        dq.append((beginWord, 1))

        while dq:
            word, step = dq.popleft()
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    next_word = f'{word[:i]}{c}{word[i + 1:]}'
                    if next_word == endWord:
                        return step + 1
                    if next_word in wordset:
                        dq.append((next_word, step + 1))
                        wordset.remove(next_word)
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        CREATED AT: 2022/2/11
        TLE
        1 <= beginWord.length <= 10
        endWord.length == beginWord.length
        1 <= wordList.length <= 5000
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        wordList = list(set(wordList))

        def one_bit_diff(w1, w2) -> bool:
            if len(w1) != len(w2):
                return False
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                if diff > 1:
                    return False
            return True if diff == 1 else False

        ret = 1
        word_dict = collections.defaultdict(set)
        # beginWord might be in list
        for i in range(len(wordList) - 1):
            if beginWord == word_dict[i]:
                ret = 0
            elif one_bit_diff(beginWord, wordList[i]):
                word_dict[beginWord].add(wordList[i])
            for j in range(i + 1, len(wordList)):
                if one_bit_diff(wordList[i], wordList[j]):
                    word_dict[wordList[i]].add(wordList[j])
                    word_dict[wordList[j]].add(wordList[i])
        if not word_dict[beginWord]:
            return 0
        # BFS
        begin_level = [beginWord]
        begin_visited = set()
        while begin_level:
            if begin_level:
                ret += 1
                next_begin_level = []

                for word in begin_level:
                    begin_visited.add(word)
                    for value in word_dict[word]:
                        if value == endWord:
                            return ret
                        if value not in begin_visited:
                            next_begin_level.append(value)
                begin_level = next_begin_level

        return 0


def test():
    assert Solution().ladderLength(
        beginWord="hit", endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert Solution().ladderLength(
        beginWord="hot", endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"]) == 4
    assert Solution().ladderLength(
        beginWord="hit", endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log"]) == 0


if __name__ == '__main__':
    test()
