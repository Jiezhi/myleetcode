#!/usr/bin/env python3
"""
CREATED AT: 2022-10-01

URL: https://leetcode.com/problems/reformat-phone-number/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1694-ReformatPhoneNumber

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        """
        Runtime: 65 ms, faster than 12.21%
        Memory Usage: 13.9 MB, less than 70.51%

        2 <= number.length <= 100
        number consists of digits and the characters '-' and ' '.
        There are at least two digits in number.
        """
        number = number.replace(' ', '').replace('-', '')
        ret = []
        i = 0
        while i + 3 <= len(number):
            ret.append(number[i:i + 3])
            i += 3
        if i == len(number) - 1:
            last = ret.pop()
            ret.append(last[:2])
            ret.append(last[-1] + number[-1])
        elif i == len(number) - 2:
            ret.append(number[-2:])
        return '-'.join(ret)


def test():
    assert Solution().reformatNumber(number="1-23-45 6") == "123-456"
    assert Solution().reformatNumber(number="123 4-567") == "123-45-67"
    assert Solution().reformatNumber(number="123 4-5678") == "123-456-78"


if __name__ == '__main__':
    test()
