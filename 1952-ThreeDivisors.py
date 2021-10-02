#!/usr/bin/env python
"""
CREATED AT: 2021/8/1
Des:
https://leetcode.com/contest/weekly-contest-252/problems/three-divisors/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                cnt += 1
        return cnt == 1


def test():
    assert not Solution().isThree(n=2)
    assert not Solution().isThree(n=8)
    assert Solution().isThree(n=4)
    assert Solution().isThree(n=9)


if __name__ == '__main__':
    test()
