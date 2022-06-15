#!/usr/bin/env python3
"""
CREATED AT: 2022-06-15

URL: https://leetcode.com/problems/longest-string-chain/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1048-LongestStringChain

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        Runtime: 187 ms, faster than 74.46% 
        Memory Usage: 14.5 MB, less than 48.74% 

        1 <= words.length <= 1000
        1 <= words[i].length <= 16
        words[i] only consists of lowercase English letters.
        """
        ret = 1
        wset = set(words)
        seen = set()
        words = sorted(words, key=len, reverse=True)
        dq = collections.deque()
        for word in words:
            if word in seen:
                continue
            dq.append((word, 1))
            while dq:
                w, cnt = dq.popleft()
                ret = max(ret, cnt)
                if w in seen:
                    continue
                seen.add(w)
                for i in range(len(w)):
                    nw = f'{w[:i]}{w[i + 1:]}'
                    if nw in wset:
                        dq.append((nw, cnt + 1))

        return ret


def test():
    assert Solution().longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    assert Solution().longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5


if __name__ == '__main__':
    test()
