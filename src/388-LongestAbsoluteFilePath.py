#!/usr/bin/env python
"""
CREATED AT: 2022/4/20
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        Runtime: 44 ms, faster than 42.82%
        Memory Usage: 13.8 MB, less than 76.26%

        1 <= input.length <= 10^4
        input may contain lowercase or uppercase English letters,
        a new line character '\n', a tab character '\t', a dot '.', a space ' ', and digits.
        """
        files = input.split('\n')
        stack = [('', 0)]
        ret = 0
        for f in files:
            fs = f.split('\t')
            while len(stack) >= len(fs) + 1:
                stack.pop()
            l = len(fs[-1]) + stack[-1][1]
            if '.' in f:
                # file
                ret = max(ret, l + len(fs) - 1)
            else:
                stack.append((fs[-1], l))
        return ret


def test():
    assert Solution().lengthLongestPath(input="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
    assert Solution().lengthLongestPath(
        input="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32


if __name__ == '__main__':
    test()
