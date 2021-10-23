#!/usr/bin/env python
"""
CREATED AT: 2021/8/9
Des:
https://leetcode.com/problems/add-strings/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3875/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from tool import print_results


class Solution:
    @print_results
    def addStrings(self, num1: str, num2: str) -> str:
        """
        317 / 317 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.3 MB
        :param num1:
        :param num2:
        :return:
        """
        # the apparent solution
        # return str(int(num1) + int(num2))
        # If the number length is large enough, we use below solution
        m = 0
        i, j = len(num1) - 1, len(num2) - 1
        ret = ''
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                tmp = int(num1[i]) + int(num2[j])
                i -= 1
                j -= 1
            elif j >= 0:
                tmp = int(num2[j])
                j -= 1
            elif i >= 0:
                tmp = int(num1[i])
                i -= 1
            m, n = divmod(tmp + m, 10)
            ret = str(n) + ret
        if m == 1:
            return '1' + ret
        else:
            return ret


def test():
    assert Solution().addStrings(num1="1", num2="9999") == '10000'
    assert Solution().addStrings(num1="11", num2="123") == '134'
    assert Solution().addStrings(num1="456", num2="77") == '533'
    assert Solution().addStrings(num1="0", num2="0") == '0'
    assert Solution().addStrings(num1="1", num2="0") == '1'
    assert Solution().addStrings(num1="5555", num2="5555") == '11110'
    assert Solution().addStrings(num1="6994", num2="36") == '7030'


if __name__ == '__main__':
    test()
