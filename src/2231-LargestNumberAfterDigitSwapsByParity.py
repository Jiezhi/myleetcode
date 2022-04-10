#!/usr/bin/env python
"""
CREATED AT: 2022/4/10
Des:

https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(int(n) for n in str(num))
        for i in range(len(num) - 1):
            for j in range(i, len(num)):
                if num[i] % 2 == num[j] % 2 and num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
        return int(''.join(str(n) for n in num))


def test():
    assert Solution().largestInteger(num=1234) == 3412
    assert Solution().largestInteger(num=65875) == 87655


if __name__ == '__main__':
    test()
