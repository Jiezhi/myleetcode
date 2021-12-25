#!/usr/bin/env python
"""
CREATED AT: 2021/12/25
Des:

https://leetcode.com/contest/biweekly-contest-68/problems/maximum-number-of-words-found-in-sentences/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        """
        1 <= sentences.length <= 100
        1 <= sentences[i].length <= 100
        sentences[i] consists only of lowercase English letters and ' ' only.
        sentences[i] does not have leading or trailing spaces.
        All the words in sentences[i] are separated by a single space.
        :param sentences:
        :return:
        """
        ret = 0
        for sentence in sentences:
            tmp_ret = len(sentence.split())
            if tmp_ret > ret:
                ret = tmp_ret
        return ret


def test():
    assert Solution().mostWordsFound(
        sentences=["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    ) == 6


if __name__ == '__main__':
    test()
