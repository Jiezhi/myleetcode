#!/usr/bin/env python
"""
CREATED AT: 2022/9/26
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

URL: https://leetcode.cn/problems/D9PW8w/
https://leetcode.cn/contest/season/2022-fall/problems/D9PW8w/
Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
        """
        1 <= path.length <= 1000
        0 <= path[i][0], path[i][1] <= 1000
        path[i][0] 与 path[i][1] 不相等
        """
        in_cnt = collections.defaultdict(set)
        out_set = set()
        points = set()
        for a, b in path:
            points.add(a)
            points.add(b)
            in_cnt[b].add(a)
            out_set.add(a)
        for k, v in in_cnt.items():
            if len(v) == len(points) - 1 and k not in out_set:
                return k
        return -1


def test():
    assert Solution().transportationHub(path=[[0, 1], [0, 3], [1, 3], [2, 0], [2, 3]]) == 3
    assert Solution().transportationHub(path=[[0, 3], [1, 0], [1, 3], [2, 0], [3, 0], [3, 2]]) == -1


if __name__ == '__main__':
    test()
