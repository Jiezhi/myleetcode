#!/usr/bin/env python
"""
CREATED AT: 2021/8/7
Des:
https://leetcode.com/problems/delete-characters-to-make-fancy-string
https://leetcode.com/contest/biweekly-contest-58/problems/delete-characters-to-make-fancy-string/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = s[:2]
        for c in s[2:]:
            if c == ret[-1] and c == ret[-2]:
                continue
            else:
                ret += c
        return ret


def test():
    assert Solution().makeFancyString(s="l") == "l"
    assert Solution().makeFancyString(s="ll") == "ll"
    assert Solution().makeFancyString(s="lll") == "ll"
    assert Solution().makeFancyString(s="leeetcode") == "leetcode"
    assert Solution().makeFancyString(s="aaabaaaa") == "aabaa"


if __name__ == '__main__':
    test()
