#!/usr/bin/env python
"""
CREATED AT: 2022/4/17
Des:
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = collections.Counter(tasks)
        ret = 0
        for k, v in cnt.items():
            if v < 2:
                return -1
            x, y = divmod(v, 3)
            if y == 1:
                ret += x + 1
            else:
                ret += x
                ret += y // 2
        return ret


def test():
    assert Solution().minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4
    assert Solution().minimumRounds(tasks=[2, 3, 3]) == -1


if __name__ == '__main__':
    test()
