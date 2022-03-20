#!/usr/bin/env python
"""
CREATED AT: 2022/3/20
Des:
https://leetcode.com/problems/find-common-characters/

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Runtime: 52 ms, faster than 88.41%
        Memory Usage: 14 MB, less than 38.04%

        1 <= words.length <= 100
        1 <= words[i].length <= 100
        words[i] consists of lowercase English letters.
        """
        cnt_list = [collections.Counter(x) for x in words]
        head = cnt_list[0]
        ret = []
        for key, value in head.items():
            for cnt in cnt_list[1:]:
                if key not in cnt:
                    value = 0
                    break
                else:
                    value = min(value, cnt[key])
            ret += [key] * value
        return ret


def test():
    assert Solution().commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]
    assert Solution().commonChars(["cool", "lock", "cook"]) == ["c", "o"]


if __name__ == '__main__':
    test()
