#!/usr/bin/env python
"""
CREATED AT: 2022/3/31
Des:
https://leetcode.com/problems/self-dividing-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        Runtime: 85 ms, faster than 33.43%
        Memory Usage: 13.8 MB, less than 75.93%

        :param left: 1 <= left <= right <= 10^4
        :param right: 1 <= left <= right <= 10^4
        :return:
        """

        def check(num: int) -> bool:
            k = num
            while k != 0:
                k, left = divmod(k, 10)
                if left == 0 or num % left != 0:
                    return False
            return True

        ret = []
        for num in range(left, right + 1):
            if check(num):
                ret.append(num)
        return ret


def test():
    assert Solution().selfDividingNumbers(left=1, right=22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


if __name__ == '__main__':
    test()
