#!/usr/bin/env python3
"""
CREATED AT: 2022-09-27

URL: https://leetcode.com/problems/push-dominoes/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 838-PushDominoes

Difficulty: Medium

Desc: 

Tag: 

See: https://leetcode.cn/problems/push-dominoes/solution/tui-duo-mi-nuo-by-leetcode-solution-dwgm/

"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Runtime: 511 ms, faster than 57.01%
        Memory Usage: 16.7 MB, less than 67.99%

        n == dominoes.length
        1 <= n <= 10^5
        dominoes[i] is either 'L', 'R', or '.'.
        """
        dominoes = list('L' + dominoes + 'R')
        n = len(dominoes)
        i, j, left = 0, 1, 'L'
        while j < n:
            while j < n and dominoes[j] == '.':
                j += 1
            right = dominoes[j]
            if left == right:
                while i < j:
                    dominoes[i] = left
                    i += 1
            elif left == 'R' and right == 'L':
                tmp = j - 1
                while i < tmp:
                    dominoes[i] = 'R'
                    dominoes[tmp] = 'L'
                    i += 1
                    tmp -= 1
            left = right
            j += 1
            i = j
        return ''.join(dominoes[1:-1])


def test():
    assert Solution().pushDominoes(dominoes="RR.L") == "RR.L"
    assert Solution().pushDominoes(dominoes=".L.R...LR..L..") == "LL.RR.LLRRLL.."


if __name__ == '__main__':
    test()
