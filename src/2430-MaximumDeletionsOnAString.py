#!/usr/bin/env python3
"""
CREATED AT: 2022-10-02

URL: https://leetcode.com/problems/maximum-deletions-on-a-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2430-MaximumDeletionsOnAString

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def deleteString(self, s: str) -> int:
        """
        1 <= s.length <= 4000
        s consists only of lowercase English letters.
        """
        n = len(s)
        pos = collections.defaultdict(list)
        for p, v in enumerate(s):
            pos[v].append(p)

        @cache
        def can(i, k) -> bool:
            cnt = k - i
            return s[i:k] == s[k:k + cnt]

        @cache
        def dp(i) -> int:
            if i >= n:
                return 0
            cpos = pos[s[i]]
            p = bisect.bisect(cpos, i)
            if p == len(cpos):
                return 1
            ret = 1
            for k in cpos[p:]:
                cnt = k - i
                if k + cnt > n:
                    break
                if can(i, k):
                    ret = max(ret, 1 + dp(k))
            return ret

        return dp(0)


def test():
    assert Solution().deleteString(s="abcabcdabc") == 2
    assert Solution().deleteString(s="aaabaab") == 4
    assert Solution().deleteString(s="aaaaa") == 5


if __name__ == '__main__':
    test()
