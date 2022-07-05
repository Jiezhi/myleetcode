#!/usr/bin/env python3
"""
CREATED AT: 2022-07-04

URL: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 395-LongestSubstringWithAtLeastKRepeatingCharacters

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import collections
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Runtime: 52 ms, faster than 79.65%
        Memory Usage: 13.9 MB, less than 89.41%

        1 <= s.length <= 10^4
        s consists of only lowercase English letters.
        1 <= k <= 10^5
        """
        if k == 1:
            return len(s)
        if k > len(s):
            return 0
        cnt = collections.Counter(s)

        possible = False
        split_key = []
        for key, value in cnt.items():
            if not possible and value >= k:
                possible = True
            if value < k:
                split_key.append(key)
        if not split_key:
            return len(s)

        if not possible:
            return 0

        dq = collections.deque([(s, '0')])
        for spk in split_key:
            while dq:
                if dq[0][1] == spk:
                    break
                node, flag = dq.popleft()
                dq.extend([(x, spk) for x in node.split(spk) if len(x) >= k])

        return max(self.longestSubstring(x[0], k) for x in dq) if dq else 0


def test():
    assert Solution().longestSubstring(s="aaabb", k=3) == 3
    assert Solution().longestSubstring(s="ababbc", k=2) == 5
    assert Solution().longestSubstring("bbaaacbd", 3) == 3
    assert Solution().longestSubstring("baaabcb", 3) == 3


if __name__ == '__main__':
    test()
