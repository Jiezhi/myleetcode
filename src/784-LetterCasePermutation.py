#!/usr/bin/env python
"""
CREATED AT: 2022/4/20
Des:
https://leetcode.com/problems/letter-case-permutation/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import string
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Runtime: 66 ms, faster than 73.58%
        Memory Usage: 15.9 MB, less than 6.60%

        1 <= s.length <= 12
        s consists of lowercase English letters, uppercase English letters, and digits.
        """
        ret = set()

        def dfs(pos, s):
            if pos >= len(s):
                return
            ret.add(s)
            dfs(pos + 1, s)

            if s[pos] in string.digits:
                return
            elif s[pos] in string.ascii_lowercase:
                new_s = f'{s[:pos]}{s[pos].upper()}{s[pos + 1:]}'
            else:
                new_s = f'{s[:pos]}{s[pos].lower()}{s[pos + 1:]}'
            ret.add(new_s)
            dfs(pos + 1, new_s)

        dfs(0, s)
        return list(ret)


def test():
    ret = Solution().letterCasePermutation("a1b2")
    ans = ['a1B2', 'A1B2', 'a1b2', 'A1b2']
    assert len(ret) == len(ans)
    for a in ans:
        assert a in ret


if __name__ == '__main__':
    test()
