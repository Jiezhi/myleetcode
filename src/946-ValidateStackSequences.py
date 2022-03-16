#!/usr/bin/env python
"""
CREATED AT: 2022/3/16
Des:
https://leetcode.com/problems/validate-stack-sequences/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Runtime: 98 ms, faster than 57.01%
        Memory Usage: 14.1 MB, less than 63.80%

        1 <= pushed.length <= 1000
        0 <= pushed[i] <= 1000
        All the elements of pushed are unique.
        popped.length == pushed.length
        popped is a permutation of pushed.
        """
        pos = pushed.index(popped[0])
        stack = pushed[:pos]
        pos += 1
        for pop in popped[1:]:
            if stack and pop == stack[-1]:
                stack.pop()
            elif pos < len(pushed) and pop == pushed[pos]:
                pos += 1
            else:
                found = False
                while pos < len(pushed):
                    if pushed[pos] == pop:
                        found = True
                        pos += 1
                        break
                    stack.append(pushed[pos])
                    pos += 1
                if pos == len(pushed) and not found:
                    return False

        return True


def test():
    assert Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    assert not Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])


if __name__ == '__main__':
    test()
