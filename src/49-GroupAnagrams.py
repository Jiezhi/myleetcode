#!/usr/bin/env python3
"""
CREATED AT: 2022-10-28

URL: https://leetcode.com/problems/group-anagrams/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3887/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 49-GroupAnagrams

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Runtime: 311 ms, faster than 10.81%
        Memory Usage: 21.6 MB, less than 9.93%

        1 <= strs.length <= 10^4
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.
        """
        cnt = collections.defaultdict(list)
        for s in strs:
            cnt[tuple(sorted(Counter(s).items()))].append(s)
        return [x for x in cnt.values()]

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """
        114 / 114 test cases passed.
        Runtime: 140 ms
        Memory Usage: 28 MB
        :param strs:
        :return:
        """
        d = collections.defaultdict(list)
        for s in strs:
            key = frozenset(collections.Counter(s).items())
            d[key].append(s)
        return list(d.values())


def test():
    ans = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    ret = Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(ans) == len(ret)
    assert Solution().groupAnagrams(strs=[""]) == [[""]]
    assert Solution().groupAnagrams(strs=["a"]) == [["a"]]


if __name__ == '__main__':
    test()
