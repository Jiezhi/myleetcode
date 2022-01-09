#!/usr/bin/env python
"""
CREATED AT: 2022/1/9
Des:

1041-RobotBoundedInCircle
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 10 min
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        Runtime: 24 ms, faster than 96.05%
        Memory Usage: 14.4 MB, less than 15.52%

        1 <= instructions.length <= 100
        ewsnstructions[i] is 'G', 'L' or, 'R'.
        :param instructions:
        :return:
        """

        pos = (0, 0)
        direction = 'N'

        def executeInstructions():
            nonlocal direction
            nonlocal pos
            for instruction in instructions:
                if instruction == 'G':
                    if direction == 'N':
                        pos = (pos[0], pos[1] + 1)
                    elif direction == 'W':
                        pos = (pos[0] - 1, pos[1])
                    elif direction == 'S':
                        pos = (pos[0], pos[1] - 1)
                    else:
                        pos = (pos[0] + 1, pos[1])
                elif instruction == 'L':
                    if direction == 'N':
                        direction = 'W'
                    elif direction == 'W':
                        direction = 'S'
                    elif direction == 'S':
                        direction = 'E'
                    elif direction == 'E':
                        direction = 'N'
                elif instruction == 'R':
                    if direction == 'N':
                        direction = 'E'
                    elif direction == 'E':
                        direction = 'S'
                    elif direction == 'S':
                        direction = 'W'
                    elif direction == 'W':
                        direction = 'N'
            return pos

        pos1 = executeInstructions()
        executeInstructions()
        pos2 = executeInstructions()
        if (pos2[0] * pos2[0] + pos2[1] * pos2[1]) > (pos1[0] * pos1[0] + pos1[1] * pos1[1]):
            return False
        return True


def test():
    assert Solution().isRobotBounded(instructions="GGLLGG")
    assert not Solution().isRobotBounded(instructions="GG")
    assert Solution().isRobotBounded(instructions="GL")


if __name__ == '__main__':
    test()
