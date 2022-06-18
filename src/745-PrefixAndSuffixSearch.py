#!/usr/bin/env python3
"""
CREATED AT: 2022-06-18

URL: https://leetcode.cn/problems/prefix-and-suffix-search/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 745-PrefixAndSuffixSearch

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
import collections
from functools import lru_cache
from typing import List


class WordFilter:
    """
    Runtime: 1037 ms, faster than 90.21%
    Memory Usage: 55.6 MB, less than 44.95%
    1 <= words.length <= 15000
    1 <= words[i].length <= 10
    1 <= prefix.length, suffix.length <= 10
    words[i], prefix and suffix consist of lower-case English letters only.
    At most 15000 calls will be made to the function f.
    """

    def __init__(self, words: List[str]):
        self.pre_dict = collections.defaultdict(set)
        self.suf_dict = collections.defaultdict(set)

        for i, w in enumerate(words):
            for j in range(1, len(w) + 1):
                self.pre_dict[w[:j]].add(i)
                self.suf_dict[w[-j:]].add(i)

    @lru_cache(None)
    def f(self, prefix: str, suffix: str) -> int:
        ret = self.pre_dict[prefix] & self.suf_dict[suffix]
        return max(ret) if ret else -1


def test():
    wf = WordFilter(
        words=["cabaabaaaa", "ccbcababac",
               "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
               "accabaccaa", "cabcbbbcca",
               "ababccabcb", "caccbbcbab", "bccbacbcba"])
    assert wf.f("bccbacbcba", "a") == 9


if __name__ == '__main__':
    test()
