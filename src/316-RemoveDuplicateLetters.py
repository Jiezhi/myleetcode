#!/usr/bin/env python
"""
CREATED AT: 2022/3/18
Des:

https://leetcode.com/problems/remove-duplicate-letters/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:  316

"""
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Runtime: 36 ms, faster than 93.32%
        Memory Usage: 14 MB, less than 54.66%

        1 <= s.length <= 10^4
        s consists of lowercase English letters.
        """
        cnt = collections.Counter(s)
        stack = []
        visited = set()

        for i, c in enumerate(s):
            if c in visited:
                cnt[c] -= 1
                continue
            while stack and c < stack[-1] and cnt[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)
            cnt[c] -= 1

        return ''.join(stack)


def test():
    assert Solution().removeDuplicateLetters("bcabc") == "abc"
    assert Solution().removeDuplicateLetters("cbacdcbc") == "acdb"
    assert Solution().removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic") == 'ilrhjfyzmnstwkboxuc'


if __name__ == '__main__':
    test()
