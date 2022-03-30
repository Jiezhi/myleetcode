#!/usr/bin/env python
"""
CREATED AT: 2022/3/30
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def interpret(self, command: str) -> str:
        """
        Runtime: 53 ms, faster than 24.27%
        Memory Usage: 13.8 MB, less than 59.09%

        1 <= command.length <= 100
        command consists of "G", "()", and/or "(al)" in some order.
        :param command:
        :return:
        """
        return command.replace('()', 'o').replace('(al)', 'al')


def test():
    assert Solution().interpret(command="G()(al)") == "Goal"
    assert Solution().interpret(command="G()()()()(al)") == "Gooooal"


if __name__ == '__main__':
    test()
