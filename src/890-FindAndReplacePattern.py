#!/usr/bin/env python3
"""
CREATED AT: 2022-07-29

URL: https://leetcode.com/problems/find-and-replace-pattern/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 890-FindAndReplacePattern

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        Runtime: 51 ms, faster than 51.73% 
        Memory Usage: 14.1 MB, less than 28.72% 

        1 <= pattern.length <= 20
        1 <= words.length <= 50
        words[i].length == pattern.length
        pattern and words[i] are lowercase English letters.
        """

        def get_hash(word: str) -> int:
            pos = collections.defaultdict(list)
            for i, c in enumerate(word):
                pos[c].append(i)
            return hash(tuple(sorted(tuple(x) for x in pos.values())))

        p = get_hash(pattern)

        return [x for x in words if get_hash(x) == p]


def test():
    assert Solution().findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb") == ["mee",
                                                                                                                 "aqq"]
    assert Solution().findAndReplacePattern(words=["a", "b", "c"], pattern="a") == ["a", "b", "c"]


if __name__ == '__main__':
    test()
