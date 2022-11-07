#!/usr/bin/env python3
"""
CREATED AT: 2022-11-07

URL: https://leetcode.com/problems/maximum-69-number/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1323-Maximum69Number

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        Runtime: 66 ms, faster than 12.89%
        Memory Usage: 13.8 MB, less than 54.69%
        1 <= num <= 10^4
        num consists of only 6 and 9 digits.
        """
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        return int(''.join(num))


def test():
    assert Solution().maximum69Number(num=9669) == 9969
    assert Solution().maximum69Number(num=9996) == 9999
    assert Solution().maximum69Number(num=9999) == 9999


if __name__ == '__main__':
    test()
