#!/usr/bin/env python
"""
CREATED AT: 2022/3/27
Des:

https://leetcode.com/problems/find-missing-observations/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Runtime: 2985 ms, faster than 13.05%
        Memory Usage: 24.3 MB, less than 44.20%

        m == rolls.length
        1 <= n, m <= 10^5
        1 <= rolls[i], mean <= 6
        """
        remain = mean * (n + len(rolls)) - sum(rolls)
        if not n <= remain <= n * 6:
            return []
        ret = [1] * n
        remain -= n
        i = 0
        while remain > 0:
            if remain >= 5:
                ret[i] += 5
                remain -= 5
                i += 1
            else:
                ret[i] += remain
                remain = 0
        return ret


def test():
    assert Solution().missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2) == [6, 6]


if __name__ == '__main__':
    test()
