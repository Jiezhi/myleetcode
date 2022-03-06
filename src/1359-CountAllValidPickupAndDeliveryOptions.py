#!/usr/bin/env python
"""
CREATED AT: 2022/3/6
Des:

https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solution/

"""


class Solution:
    def countOrders(self, n: int) -> int:
        """
        1 <= n <= 500
        """
        ret = 1
        modulo = 10 ** 9 + 7
        for i in range(2, n + 1):
            ret *= (2 * i - 1) * i
            ret %= modulo
        return ret


def test():
    assert Solution().countOrders(n=2) == 6
    assert Solution().countOrders(n=3) == 90


if __name__ == '__main__':
    test()
