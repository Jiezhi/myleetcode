#!/usr/bin/env python
"""
CREATED AT: 2021/10/16
Des:

https://leetcode.com/contest/biweekly-contest-63/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        1 <= colors.length <= 10**5
        colors consists of only the letters 'A' and 'B'
        :param colors:
        :return:
        """
        if len(colors) < 3:
            return False
        a_turns = 0
        b_turns = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a_turns += 1
                else:
                    b_turns += 1
        return a_turns > b_turns


def test():
    assert Solution().winnerOfGame(colors="AAABABB")
    assert not Solution().winnerOfGame(colors="AA")
    assert not Solution().winnerOfGame(colors="ABBBBBBBAAA")


if __name__ == '__main__':
    test()
