#!/usr/bin/env python
"""
CREATED AT: 2022-06-01
Des: https://leetcode.com/problems/matchsticks-to-square/

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Runtime: 279 ms, faster than 81.04% 
        Memory Usage: 18.6 MB, less than 24.17% 

        1 <= matchsticks.length <= 15
        1 <= matchsticks[i] <= 10^8
        """
        l, m = divmod(sum(matchsticks), 4)
        if m > 0 or any(x > l for x in matchsticks):
            return False

        matchsticks.sort(reverse=True)
        stack = [(1, matchsticks[0], 0, 0, 0)]
        seen = set()

        while stack:
            node = stack.pop()
            pos, borders = node[0], node[1:]
            if all(x == l for x in borders):
                return True
            if pos >= len(matchsticks) or any(x > l for x in borders):
                continue
            if tuple(sorted(borders)) in seen:
                continue
            seen.add(tuple(sorted(borders)))
            value = matchsticks[pos]
            stack.append((pos + 1, borders[0] + value, borders[1], borders[2], borders[3]))
            stack.append((pos + 1, borders[0], borders[1] + value, borders[2], borders[3]))
            stack.append((pos + 1, borders[0], borders[1], borders[2] + value, borders[3]))
            stack.append((pos + 1, borders[0], borders[1], borders[2], borders[3] + value))

        return False


def test():
    assert Solution().makesquare(matchsticks=[1, 1, 2, 2, 2])
    assert not Solution().makesquare(matchsticks=[3, 3, 3, 3, 4])
    assert not Solution().makesquare(
        [7215807, 6967211, 5551998, 6632092, 2802439, 821366, 2465584, 9415257, 8663937, 3976802, 2850841, 803069,
         2294462, 8242205, 9922998])


if __name__ == '__main__':
    test()
