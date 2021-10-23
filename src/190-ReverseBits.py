#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:
https://leetcode.com/problems/reverse-bits/
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from tool import print_results


class Solution:
    @print_results
    def reverseBits(self, n: int) -> int:
        """
        600 / 600 test cases passed.
        Status: Accepted
        Runtime: 20 ms
        Memory Usage: 14.3 MB
        :param n:
        :return:
        """
        reversed_n = format(n, 'b')[::-1]
        reversed_n += '0' * (32 - len(reversed_n))
        return int(reversed_n, 2)


def test():
    assert Solution().reverseBits(n=43261596) == 964176192
    assert Solution().reverseBits(n=0b00000010100101000001111010011100) == 964176192
    assert Solution().reverseBits(n=0b11111111111111111111111111111101) == 3221225471


if __name__ == '__main__':
    test()
