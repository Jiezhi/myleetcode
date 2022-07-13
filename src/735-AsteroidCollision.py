#!/usr/bin/env python3
"""
CREATED AT: 2022-07-13

URL: https://leetcode.c/problems/asteroid-collision/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 735-AsteroidCollision

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Runtime: 92 ms, faster than 99.20% 
        Memory Usage: 15.3 MB, less than 24.45% 

        2 <= asteroids.length <= 10^4
        -1000 <= asteroids[i] <= 1000
        asteroids[i] != 0
        """
        stack = []
        for cur in asteroids:
            if cur > 0:
                stack.append(cur)
            elif stack:
                while stack:
                    if -cur == stack[-1]:
                        stack.pop()
                        break
                    if stack[-1] < 0:
                        stack.append(cur)
                        break
                    if -cur > stack[-1]:
                        stack.pop()
                        if not stack:
                            stack.append(cur)
                            break
                    else:
                        break
            else:
                stack.append(cur)
        return stack


def test():
    assert Solution().asteroidCollision(asteroids=[5, 10, -5]) == [5, 10]
    assert Solution().asteroidCollision(asteroids=[5, 10, -5, -11]) == [-11]
    assert Solution().asteroidCollision(asteroids=[8, -8]) == []
    assert Solution().asteroidCollision(asteroids=[10, 2, -5]) == [10]


if __name__ == '__main__':
    test()
