#!/usr/bin/env python3
"""
CREATED AT: 2022/5/19
Des:

https://leetcode.cn/problems/minimum-window-substring/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: https://leetcode.com/problems/minimum-window-substring/solution/

"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        AC: 06/07/2022
        Ref: https://leetcode.com/problems/minimum-window-substring/solution/
        Runtime: 232 ms, faster than 28.69%
        Memory Usage: 14.7 MB, less than 36.10%

        m == s.length
        n == t.length
        1 <= m, n <= 10^5
        s and t consist of uppercase and lowercase English letters.
        """
        m, n = len(s), len(t)
        if m < n:
            return ''

        ret, cnt = s + '0', 0
        cnt_s, cnt_t = Counter(), Counter(t)
        l, r = 0, 0
        while l < m:
            print(ret)
            if cnt == n:
                if len(ret) > r - l:
                    ret = s[l:r]
                if len(ret) == n:
                    return ret
                if s[l] in cnt_t:
                    cnt_s[s[l]] -= 1
                    if cnt_s[s[l]] < cnt_t[s[l]]:
                        cnt -= 1
                l += 1
            elif r < m:
                if s[r] in cnt_t:
                    cnt_s[s[r]] += 1
                    if cnt_s[s[r]] <= cnt_t[s[r]]:
                        cnt += 1
                r += 1
            else:
                break
        return '' if len(ret) == m + 1 else ret


def test():
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="ab", t="a") == "a"


if __name__ == '__main__':
    test()
