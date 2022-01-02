#!/usr/bin/env python
"""
CREATED AT: 2022/1/2
Des:

https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Ref: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        Ref: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60
        Runtime: 208 ms, faster than 97.68%
        Memory Usage: 18 MB, less than 48.64%
        1 <= time.length <= 6 * 10^4
        1 <= time[i] <= 500
        :param time:
        :return:
        """
        remainders = [0] * 60
        ret = 0
        for t in time:
            ret += remainders[-t % 60]
            remainders[t % 60] += 1
        return ret


def test():
    assert Solution().numPairsDivisibleBy60(time=[30, 20, 150, 100, 40]) == 3
    assert Solution().numPairsDivisibleBy60(time=[60]) == 0
    assert Solution().numPairsDivisibleBy60(time=[60, 60]) == 1
    assert Solution().numPairsDivisibleBy60(time=[60, 60, 60]) == 3
    assert Solution().numPairsDivisibleBy60(time=[60, 60, 60, 60]) == 6
    assert Solution().numPairsDivisibleBy60(time=[60, 60, 60, 60, 60]) == 10


if __name__ == '__main__':
    test()
