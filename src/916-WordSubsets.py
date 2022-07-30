#!/usr/bin/env python3
"""
CREATED AT: 2022-07-30

URL: https://leetcode.cn/problems/word-subsets/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 916-WordSubsets

Difficulty: 

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Runtime: 1086 ms, faster than 66.67%
        Memory Usage: 20 MB, less than 12.00%

        1 <= words1.length, words2.length <= 10^4
        1 <= words1[i].length, words2[i].length <= 10
        words1[i] and words2[i] consist only of lowercase English letters.
        All the strings of words1 are unique.
        """
        word_cnt = [collections.Counter(x) for x in set(words2)]
        most_cnt = collections.defaultdict(int)
        for cnt in word_cnt:
            for c in cnt.keys():
                most_cnt[c] = max(most_cnt[c], cnt[c])

        def allSubset(word: str) -> bool:
            cnt = collections.Counter(word)
            for c in most_cnt.keys():
                if cnt[c] < most_cnt[c]:
                    return False
            return True

        return [x for x in words1 if allSubset(x)]


def test():
    assert Solution().wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "o"]) == [
        "facebook", "google", "leetcode"]


if __name__ == '__main__':
    test()
