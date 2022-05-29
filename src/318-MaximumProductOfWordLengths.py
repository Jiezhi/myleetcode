#!/usr/bin/env python
"""
CREATED AT: 2022/5/29
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Runtime: 766 ms, faster than 65.35%
        Memory Usage: 15.9 MB, less than 18.04%
        :param words:
        2 <= words.length <= 1000
        1 <= words[i].length <= 1000
        words[i] consists only of lowercase English letters.
        :return:
        """
        ret = 0
        words = sorted([(len(x), set(x)) for x in words], reverse=True)
        for i, v in enumerate(words):
            for j in range(i + 1, len(words)):
                curr_len, curr_set = words[j]
                if curr_len * v[0] <= ret:
                    break
                if curr_set.isdisjoint(v[1]):
                    ret = max(ret, curr_len * v[0])
                    break

        return ret


def test():
    pass


if __name__ == '__main__':
    test()
