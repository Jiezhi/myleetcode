#!/usr/bin/env python
"""
CREATED AT: 2021/12/26
Des:

https://leetcode.com/contest/weekly-contest-273/problems/a-number-after-a-double-reversal
https://leetcode.com/problems/a-number-after-a-double-reversal/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        """
        0 <= num <= 10^6
        :param num:
        :return:
        """
        return not ((num % 10) == 0 and num > 0)


def test():
    assert Solution().isSameAfterReversals(num=0)
    assert Solution().isSameAfterReversals(num=526)
    assert not Solution().isSameAfterReversals(num=5260)


if __name__ == '__main__':
    test()
