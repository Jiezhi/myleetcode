#!/usr/bin/env python3
"""
CREATED AT: 2022-10-19

URL: https://leetcode.com/problems/top-k-frequent-words/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 692-TopKFrequentWords

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Runtime: 56 ms, faster than 96.72%
        Memory Usage: 14 MB, less than 27.71%

        1 <= words.length <= 500
        1 <= words[i].length <= 10
        words[i] consists of lowercase English letters.
        k is in the range [1, The number of unique words[i]]
        """
        return [word for word, _ in sorted(Counter(words).items(), key=lambda x: [-x[1], x[0]])[:k]]


def test():
    assert Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding", "like", "like"], k=2) == ["i",
                                                                                                                    "like"]
    assert Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2) == ["i", "love"]
    assert Solution().topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                                   k=4) == ["the", "is", "sunny", "day"]


if __name__ == '__main__':
    test()
