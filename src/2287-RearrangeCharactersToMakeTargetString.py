#!/usr/bin/env python3
"""
CREATED AT: 2023-01-15

URL:

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2287-RearrangeCharactersToMakeTargetString

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
import collections


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnts, cntt = collections.Counter(s), collections.Counter(target)
        return min(cnts[k] // cntt[k] for k in cntt.keys())


def test():
    assert Solution().rearrangeCharacters(s="ilovecodingonleetcode", target="code") == 2
    assert Solution().rearrangeCharacters(s="abcba", target="abc") == 1


if __name__ == '__main__':
    test()
