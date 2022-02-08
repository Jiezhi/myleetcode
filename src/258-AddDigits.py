#!/usr/bin/env python
"""
CREATED AT: 2021/10/2
Des:
https://leetcode.com/problems/add-digits/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""


class Solution:
    def addDigits(self, num: int) -> int:
        """
        Just print 0~50 to see the result.
        Runtime: 48 ms, faster than 37.91%
        Memory Usage: 13.8 MB, less than 91.66%
        0 <= num <= 2^31 - 1
        :param num:
        :return:
        """
        if num == 0:
            return 0
        num = num % 9
        return 9 if num == 0 else num

    def addDigits2(self, num: int) -> int:
        """
        0 <= num <= 2^31 - 1
        :param num:
        :return:
        """
        if 0 <= num < 10:
            return num
        new_num = 0
        while num != 0:
            num, left = divmod(num, 10)
            new_num += left
        return self.addDigits(new_num)


def test():
    assert Solution().addDigits(num=38) == 2
    assert Solution().addDigits(num=0) == 0


if __name__ == '__main__':
    test()
