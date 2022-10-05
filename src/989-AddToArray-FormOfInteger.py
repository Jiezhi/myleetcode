#!/usr/bin/env python3
"""
CREATED AT: 2022-10-05

URL: https://leetcode.com/problems/add-to-array-form-of-integer/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 989-AddToArray-FormOfInteger

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
        Runtime: 784 ms, faster than 21.69%
        Memory Usage: 15.2 MB, less than 27.21%

        1 <= num.length <= 10^4
        0 <= num[i] <= 9
        num does not contain any leading zeros except for the zero itself.
        1 <= k <= 10^4
        """
        return [int(x) for x in list(str(int(''.join([str(n) for n in num])) + k))]


def test():
    assert Solution().addToArrayForm(num=[1, 2, 0, 0], k=34) == [1, 2, 3, 4]
    assert Solution().addToArrayForm(num=[2, 7, 4], k=181) == [4, 5, 5]
    assert Solution().addToArrayForm(num=[2, 1, 5], k=806) == [1, 0, 2, 1]


if __name__ == '__main__':
    test()
