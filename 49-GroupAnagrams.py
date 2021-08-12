#!/usr/bin/env python
"""
CREATED AT: 2021/8/12
Des:
https://leetcode.com/problems/group-anagrams/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3887/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/group-anagrams/discuss/1398888/Python-Group-by-sorted-string-group-by-count-characters-Solutions-Clean-and-Concise
"""
import collections
from typing import List

from tool import print_results


class Solution:
    @print_results
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        114 / 114 test cases passed.
        Status: Accepted
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
    # just check the length of the result, maybe add check the content next time.
    assert len(ans) == len(ret)
    assert Solution().groupAnagrams(strs=[""]) == [[""]]
    assert Solution().groupAnagrams(strs=["a"]) == [["a"]]


if __name__ == '__main__':
    test()
