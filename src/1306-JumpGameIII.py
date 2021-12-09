#!/usr/bin/env python
"""
CREATED AT: 2021/12/9
Des:

https://leetcode.com/problems/jump-game-iii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Time Spent: 6 min
"""
import collections
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Runtime: 300 ms, faster than 64.24% of Python3
        Memory Usage: 21.2 MB, less than 57.95% of Python3

        1 <= arr.length <= 5 * 10^4
        0 <= arr[i] < arr.length
        0 <= start < arr.length
        :param arr:
        :param start:
        :return:
        """
        if not arr:
            return False
        dq = collections.deque()
        dq.append(start)
        loc_sets = set()
        loc_sets.add(start)
        while len(dq) > 0:
            pos = dq.pop()
            if arr[pos] == 0:
                return True
            pre_pos, nxt_pos = pos - arr[pos], pos + arr[pos]
            if pre_pos >= 0 and pre_pos not in loc_sets:
                dq.append(pre_pos)
                loc_sets.add(pre_pos)
            if nxt_pos < len(arr) and nxt_pos not in loc_sets:
                dq.append(nxt_pos)
                loc_sets.add(nxt_pos)
        return False


def test():
    assert Solution().canReach(arr=[0], start=0)
    assert not Solution().canReach(arr=[1], start=0)
    assert Solution().canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5)
    assert Solution().canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0)
    assert not Solution().canReach(arr=[3, 0, 2, 1, 2], start=2)


if __name__ == '__main__':
    test()
