#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/16

Leetcode: https://leetcode.com/problems/k-th-symbol-in-grammar/

https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/

"""
import math


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # Do some tricks
        # The first always be 0
        if K == 1:
            return 0
        last = self.kthGrammar(N - 1, math.ceil(K / 2))
        if K % 2 == 1:
            return 0 if last == 0 else 1
        else:
            return 1 if last == 0 else 0


def test():
    assert Solution().kthGrammar(N=1, K=1) == 0
    assert Solution().kthGrammar(N=2, K=1) == 0
    assert Solution().kthGrammar(N=2, K=2) == 1
    assert Solution().kthGrammar(N=4, K=5) == 1


if __name__ == '__main__':
    test()

    # print(Solution().kthGrammar(N=30, K=2))
