#!/usr/bin/env python
"""
CREATED AT: 2022/5/6
Des:
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 1047-RemoveAllAdjacentDuplicatesInString.py

"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Runtime: 121 ms, faster than 79.09%
        Memory Usage: 18.1 MB, less than 77.09%

        1 <= s.length <= 10^5
        2 <= k <= 10^4
        s only contains lower case English letters.
        """
        ret = []
        pre = None
        cnt = 0
        for c in s:
            if cnt == 0:
                pre = c
                cnt = 1
            elif c == pre:
                cnt += 1
                if cnt == k:
                    pre, cnt = ret.pop() if ret else (None, 0)
            else:
                ret.append((pre, cnt))
                pre, cnt = c, 1
        return ''.join([c * cnt for c, cnt in ret] + [pre] * cnt)


def test():
    assert Solution().removeDuplicates(s="deeedbbcccbdaa", k=3) == "aa"
    assert Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2) == "ps"


if __name__ == '__main__':
    test()
