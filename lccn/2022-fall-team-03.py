"""
CREATED AT: 2022/10/7
Des:

GITHUB: https://github.com/Jiezhi/myleetcode
https://leetcode.cn/contest/season/2022-fall/problems/1GxJYY/
https://leetcode.cn/problems/1GxJYY/
Difficulty: Easy

Tag:

See:

Time Spent:  min
"""
from collections import Counter, defaultdict
from typing import List, Optional

from src.tree_node import TreeNode


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        mod = 10 ** 9 + 7
        n = len(flowers)
        dc = defaultdict(int)
        ret = 0

        i, j = 0, 0
        while j < n:
            dc[flowers[j]] += 1
            while i <= j and dc[flowers[j]] > cnt:
                dc[flowers[i]] -= 1
                i += 1
            ret += j - i + 1
            ret %= mod
            j += 1
        return ret


def test():
    assert Solution().beautifulBouquet(flowers=[1, 2, 3, 2], cnt=1) == 8


if __name__ == '__main__':
    test()
