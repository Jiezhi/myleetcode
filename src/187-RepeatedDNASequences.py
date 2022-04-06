#!/usr/bin/env python
"""
CREATED AT: 2022/4/6
Des:
https://leetcode.com/problems/repeated-dna-sequences/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Runtime: 100 ms, faster than 48.73%
        Memory Usage: 27.7 MB, less than 37.69%

        1 <= s.length <= 10^5
        s[i] is either 'A', 'C', 'G', or 'T'.
        :param s:
        :return:
        """
        cnt = collections.defaultdict(int)
        for i in range(len(s) - 9):
            cnt[s[i:i + 10]] += 1
        return [k for k, v in cnt.items() if v > 1]


def test():
    assert Solution().findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") in [["AAAAACCCCC", "CCCCCAAAAA"],
                                                                                         ["CCCCCAAAAA", "AAAAACCCCC"]]
    assert Solution().findRepeatedDnaSequences(s="AAAAAAAAAAAA") == ["AAAAAAAAAA"]


if __name__ == '__main__':
    test()
