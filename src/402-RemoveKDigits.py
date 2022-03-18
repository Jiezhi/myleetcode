#!/usr/bin/env python
"""
CREATED AT: 2022/3/18
Des:

https://leetcode.com/problems/remove-k-digits/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Runtime: 189 ms, faster than 10.50%
        Memory Usage: 71 MB, less than 7.56%

        1 <= k <= num.length <= 10^5
        num consists of only digits.
        num does not have any leading zeros except for the zero itself.
        """

        def remove(s: str, k: int, pos: int) -> str:
            if len(s) == k:
                return '0'

            if k == 0:
                return str(int(s))

            for i in range(pos, len(s) - 1):
                if int(s[i]) > int(s[i + 1]):
                    return remove(f'{s[:i]}{s[i + 1:]}', k - 1, i - 1 if i > 0 else 0)
            return remove(s[:-k], 0, 0)

        return remove(num, k, 0)


def test():
    assert Solution().removeKdigits('1432219', 3) == '1219'
    assert Solution().removeKdigits('10200', 1) == '200'
    assert Solution().removeKdigits('10', 2) == '0'
    assert Solution().removeKdigits('1234567890', 9) == '0'


if __name__ == '__main__':
    test()
