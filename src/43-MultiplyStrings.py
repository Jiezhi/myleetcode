#!/usr/bin/env python
"""
CREATED AT: 2021/12/8
Des:

Given two non-negative integers num1 and num2 represented as strings,
 return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library
or convert the inputs to integer directly.


https://leetcode.com/problems/multiply-strings/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: https://leetcode.com/problems/multiply-strings/solution/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Runtime: 434 ms, faster than 5.05% of Python3
        Memory Usage: 14.4 MB, less than 11.54% of Python3

        1 <= num1.length, num2.length <= 200
        num1 and num2 consist of digits only.
        Both num1 and num2 do not contain any leading zero, except the number 0 itself.
        :param num1:
        :param num2:
        :return:
        """
        if len(num1) == 0 or len(num2) == 0:
            return ""
        if num1 == '0' or num2 == '0':
            return '0'

        def mul(mul1: str, mul2: str, offset: int) -> str:
            carrier = 0
            mul2 = int(mul2)
            mul1 = list(mul1)
            for i in range(len(mul1) - 1, -1, -1):
                carrier, tmp = divmod(int(mul1[i]) * mul2 + carrier, 10)
                mul1[i] = str(tmp)

            mul1 = ''.join(mul1)
            if carrier > 0:
                mul1 = str(carrier) + mul1

            mul1 += '0' * offset
            return mul1

        def plus(p1, p2) -> str:
            tmp_ret = list()
            carrier = 0
            i, j = len(p1) - 1, len(p2) - 1
            while i >= 0 or j >= 0:
                if i >= 0:
                    num1 = int(p1[i])
                    i -= 1
                else:
                    num1 = 0
                if j >= 0:
                    num2 = int(p2[j])
                    j -= 1
                else:
                    num2 = 0
                carrier, tmp = divmod(num1 + num2 + carrier, 10)
                tmp_ret.insert(0, str(tmp))
            if carrier > 0:
                tmp_ret.insert(0, str(carrier))
            return ''.join(tmp_ret)

        ret = '0'
        for i in range(len(num1) - 1, -1, -1):
            tmp_ret = mul(num2, num1[i], len(num1) - i - 1)
            ret = plus(ret, tmp_ret)
        return ret


def test():
    assert Solution().multiply(num1="2", num2="3") == "6"
    assert Solution().multiply(num1="111112", num2="0") == "0"
    assert Solution().multiply(num1="123", num2="456") == "56088"
    assert Solution().multiply(num1="123456789", num2="987654321") == "121932631112635269"


if __name__ == '__main__':
    test()
