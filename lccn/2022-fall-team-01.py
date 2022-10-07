"""
CREATED AT: 2022/10/7
Des:

GITHUB: https://github.com/Jiezhi/myleetcode
https://leetcode.cn/contest/season/2022-fall/problems/600YaG/
https://leetcode.cn/problems/600YaG/
Difficulty: Easy

Tag:

See:

Time Spent:  min
"""
from collections import Counter
from typing import List


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        ret = [0] * 26
        ord_a = ord('a')
        for s in demand:
            for k, v in Counter(s).items():
                pos = ord(k) - ord_a
                ret[pos] = max(ret[pos], v)
        return sum(ret)


def test():
    assert Solution().minNumBooths(demand=["acd", "bed", "accd"]) == 6
    assert Solution().minNumBooths(demand=["abc", "ab", "ac", "b"]) == 3


if __name__ == '__main__':
    test()
