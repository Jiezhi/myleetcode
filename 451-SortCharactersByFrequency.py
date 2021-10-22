#!/usr/bin/env python
"""
CREATED AT: 2021/10/22
Des:

https://leetcode.com/problems/sort-characters-by-frequency/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Runtime: 73 ms, faster than 29.61%
        Memory Usage: 15.1 MB, less than 99.90%
        1 <= s.length <= 5 * 10**5
        s consists of uppercase and lowercase English letters and digits.
        :param s:
        :return:
        """
        return ''.join(k * v for k, v in collections.Counter(s).most_common())


def test():
    assert Solution().frequencySort(s="tree") in ['eetr', 'eert']
    assert Solution().frequencySort(s="cccaaa") in ['cccaaa', 'aaaccc']
    assert Solution().frequencySort(s="cccaa") in ['cccaa']


if __name__ == '__main__':
    test()
