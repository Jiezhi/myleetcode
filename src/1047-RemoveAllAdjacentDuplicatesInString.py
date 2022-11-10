#!/usr/bin/env python3
"""
CREATED AT: 2022-11-10

URL: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1047-RemoveAllAdjacentDuplicatesInString

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Runtime: 214 ms, faster than 38.96%
        Memory Usage: 14.8 MB, less than 52.58%
        1 <= s.length <= 10^5
        s consists of lowercase English letters.
        """
        ret = []
        for c in s:
            if not ret or ret[-1] != c:
                ret.append(c)
            else:
                ret.pop()
        return ''.join(ret)


def test():
    assert Solution().removeDuplicates(s="a") == "a"
    assert Solution().removeDuplicates(s="aa") == ""
    assert Solution().removeDuplicates(s="abbaca") == "ca"
    assert Solution().removeDuplicates(s="azxxzy") == "ay"


if __name__ == '__main__':
    test()
