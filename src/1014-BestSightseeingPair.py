#!/usr/bin/env python
"""
CREATED AT: 2022/2/28
Des:

https://leetcode.com/problems/best-sightseeing-pair/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        Runtime: 556 ms, faster than 69.00%
        Memory Usage: 20.7 MB, less than 18.01%

        2 <= values.length <= 5 * 10^4
        1 <= values[i] <= 1000
        """
        ret = values[0] + values[1] - 1
        # store the max pair score and positions of i, j
        pre_pair = (ret, (0, 1))
        for i in range(2, len(values)):
            # we calculate the max pair score with pre best pair of i, j
            p1 = pre_pair[1][0]
            p2 = pre_pair[1][1]
            v1 = values[p1] + values[i] + p1 - i
            v2 = values[p2] + values[i] + p2 - i
            if v2 > v1:
                pre_pair = (v2, (p2, i))
            else:
                pre_pair = (v1, (p1, i))
            ret = max(ret, pre_pair[0])
        return ret


def test():
    assert Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11


if __name__ == '__main__':
    test()
