#!/usr/bin/env python3
"""
CREATED AT: 2022-09-08

URL: https://leetcode.com/problems/beautiful-arrangement/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 526-BeautifulArrangement

Difficulty: Medium

Desc: 

Tag: 

See: 667

"""


class Solution:
    def countArrangement(self, n: int) -> int:
        """
        Runtime: 5063 ms, faster than 5.07%
        Memory Usage: 13.8 MB, less than 76.58%

        1 <= n <= 15
        """
        ret = 0
        stack = [(1, '1' * n)]
        while stack:
            pos, left = stack.pop()
            if pos == n + 1:
                ret += 1
                continue
            for i in range(1, n + 1):
                if left[i - 1] == '1' and (i % pos == 0 or pos % i == 0):
                    stack.append((pos + 1, f'{left[:i - 1]}0{left[i:]}'))
        return ret


def test():
    assert Solution().countArrangement(n=2) == 2
    assert Solution().countArrangement(n=1) == 1


if __name__ == '__main__':
    test()
