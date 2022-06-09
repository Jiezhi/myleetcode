#!/usr/bin/env python3
"""
CREATED AT: 2022-06-09

Des: https://leetcode.com/problems/word-break-ii/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 140-WordBreakII

Difficulty: Hard

Tag: 

See: 

"""
from functools import lru_cache
from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def stop_pos(self, word: str) -> List[int]:
        word += '#'
        ret = []
        cur = self.root
        depth = 0
        for c in word:
            if '#' in cur:
                ret.append(depth)
            if c not in cur:
                break
            cur = cur[c]
            depth += 1
        return ret


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Runtime: 45 ms, faster than 42.91%
        Memory Usage: 14 MB, less than 31.45%
        1 <= s.length <= 20
        1 <= wordDict.length <= 1000
        1 <= wordDict[i].length <= 10
        s and wordDict[i] consist of only lowercase English letters.
        All the strings of wordDict are unique.
        """
        trie = Trie()
        for word in wordDict:
            trie.add(word)

        @lru_cache(None)
        def dp(pos: int) -> List[str]:
            if pos >= len(s):
                return []
            p = trie.stop_pos(s[pos:])
            if not p:
                return []
            ret = []
            for i in p:
                pre_word = s[pos:pos + i]
                next_ret = dp(pos + i)
                if not next_ret:
                    ret.append(pre_word)
                    continue
                for j in next_ret:
                    r = f'{pre_word} {j}'
                    if len(r) - r.count(' ') == len(s) - pos:
                        ret.append(r)
            return ret

        # return dp(0)
        return [x for x in dp(0) if len(x) - x.count(' ') == len(s)]


def test():
    ans = ["aaa aaaa", "aaaa aaa"]
    ret = Solution().wordBreak(s="aaaaaaa", wordDict=["aaa", "aaaa"])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret

    ans = ["cats and dog", "cat sand dog"]
    ret = Solution().wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret

    ans = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    ret = Solution().wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret


if __name__ == '__main__':
    test()
