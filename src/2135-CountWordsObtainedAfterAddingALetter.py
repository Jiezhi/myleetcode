#!/usr/bin/env python
"""
CREATED AT: 2022/1/9
Des:

https://leetcode.com/problems/count-words-obtained-after-adding-a-letter
https://leetcode.com/contest/weekly-contest-275/problems/count-words-obtained-after-adding-a-letter/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        """
        1 <= startWords.length, targetWords.length <= 5 * 10^4
        1 <= startWords[i].length, targetWords[j].length <= 26
        Each string of startWords and targetWords consists of lowercase English letters only.
        No letter occurs more than once in any string of startWords or targetWords.
        :param startWords:
        :param targetWords:
        :return:
        """
        # preprocess startWords, save all possibles
        words_set = set()
        for sw in startWords:
            sw_bit = 0
            for c in sw:
                sw_bit |= (1 << (ord(c) - ord('a')))
            for i in range(26):
                if sw_bit & (1 << i) == 0:
                    words_set.add(sw_bit | (1 << i))

        ret = 0
        for tw in targetWords:
            tw_bit = 0
            for c in tw:
                tw_bit |= (1 << (ord(c) - ord('a')))
            if tw_bit in words_set:
                ret += 1
        return ret


def test():
    assert Solution().wordCount(["mox", "bj", "rsy", "jqsh"], ["trk", "vjb", "jkr"]) == 1
    assert Solution().wordCount(startWords=["ant", "act", "tack"], targetWords=["tack", "act", "acti"]) == 2
    assert Solution().wordCount(startWords=["ab", "a"], targetWords=["abc", "abcd"]) == 1


if __name__ == '__main__':
    test()
