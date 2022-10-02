#!/usr/bin/env python3
"""
CREATED AT: 2022-10-02

URL: https://leetcode.com/problems/number-of-common-factors/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2427-NumberOfCommonFactors

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """
        1 <= a, b <= 1000
        """
        return sum(1 for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0)


def test():
    assert Solution().commonFactors(a=12, b=6) == 4
    assert Solution().commonFactors(a=25, b=30) == 2


if __name__ == '__main__':
    test()
