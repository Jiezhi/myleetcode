#!/usr/bin/env python3
"""
CREATED AT: 2022-07-20

URL: https://leetcode.com/problems/number-of-matching-subsequences/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 792-NumberOfMatchingSubsequences

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import collections
import bisect
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        Runtime: 706 ms, faster than 58.19% 
        Memory Usage: 17.2 MB, less than 24.29%
        1 <= s.length <= 5 * 10^4
        1 <= words.length <= 5000
        1 <= words[i].length <= 50
        s and words[i] consist of only lowercase English letters.
        """
        pos = collections.defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        ret = 0
        for word in words:
            if len(word) >= len(s):
                if word == s:
                    ret += 1
                continue
            cur = 0
            found = True
            for c in word:
                if c not in pos:
                    found = False
                    break
                index = bisect.bisect_left(pos[c], cur)
                if index == len(pos[c]):
                    found = False
                    break
                cur = pos[c][index] + 1
            if found:
                ret += 1
        return ret


def test():
    assert Solution().numMatchingSubseq(s = "abcde", words = ["a", "", "ae", "bb","acd","ace"]) == 5
    assert Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]) == 3
    assert Solution().numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2


if __name__ == '__main__':
    test()

