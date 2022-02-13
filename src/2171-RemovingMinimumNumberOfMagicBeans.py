#!/usr/bin/env python
"""
CREATED AT: 2022/2/13
Des:

https://leetcode.com/problems/removing-minimum-number-of-magic-beans/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 45 min
"""
import collections
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        """
        Runtime: 1642 ms, faster than 62.50%
        Memory Usage: 37.3 MB, less than 12.50%

        1 <= beans.length <= 10^5
        1 <= beans[i] <= 10^5
        """
        n = len(beans)
        bean_sum = sum(beans)
        beans = sorted(collections.Counter(beans).items())
        ret = bean_sum
        acc_sum = 0
        acc_cnt = 0
        for key, value in beans:
            acc_cnt += value
            ret = min(ret, bean_sum - key * value - (n - acc_cnt) * key)
            acc_sum += key * value
        return ret


def test():
    assert Solution().minimumRemoval(beans=[4, 1, 6, 5]) == 4
    assert Solution().minimumRemoval(beans=[2, 10, 3, 2]) == 7


if __name__ == '__main__':
    test()
