#!/usr/bin/env python
"""
CREATED AT: 2022/5/25
Des:
https://leetcode.com/problems/russian-doll-envelopes/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 300

"""
import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Runtime: 1531 ms, faster than 59.66%
        Memory Usage: 61.6 MB, less than 67.23%
        :param envelopes:
        1 <= envelopes.length <= 10^5
        envelopes[i].length == 2
        1 <= wi, hi <= 10^5
        :return:
        """
        nums = [x for _, x in sorted(envelopes, key=lambda e: (e[0], -e[1]))]

        ret = [nums[0]]

        for num in nums[1:]:
            if num > ret[-1]:
                ret.append(num)
            else:
                pos = bisect.bisect_left(ret, num)
                ret[pos] = num
        return len(ret)

    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        """
        LTE
        :param envelopes:
        1 <= envelopes.length <= 10^5
        envelopes[i].length == 2
        1 <= wi, hi <= 10^5
        :return:
        """
        env = [x for _, x in sorted(envelopes, key=lambda e: (e[0], -e[1]))]

        n = len(env)

        dp = [1] * n

        for i in range(1, n):
            dp[i] = max(dp[j] + 1 if env[j] < env[i] else 1 for j in range(i))

        return max(dp)


def test():
    assert Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1


if __name__ == '__main__':
    test()
