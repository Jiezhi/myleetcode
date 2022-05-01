#!/usr/bin/env python
"""
CREATED AT: 2022/5/1
Des:
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        2 <= number.length <= 100
        number consists of digits from '1' to '9'.
        digit is a digit from '1' to '9'.
        digit occurs at least once in number.
        """
        pos = number.index(digit)
        if pos == len(number):
            return number[:-1]
        ret = f'{number[:pos]}{number[pos + 1:]}'
        for i in range(pos + 1, len(number)):
            if number[i] == digit:
                tmp_ret = f'{number[:i]}{number[i + 1:]}'
                if int(tmp_ret) > int(ret):
                    ret = tmp_ret
        return ret


def test():
    assert Solution().removeDigit(number="123", digit="3") == "12"
    assert Solution().removeDigit(number="1231", digit="1") == "231"


if __name__ == '__main__':
    test()
