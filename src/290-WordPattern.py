"""
CREATED AT: 2022/1/17
Des:

https://leetcode.com/problems/word-pattern/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag:

See:

Time Spent: 5 min
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Runtime: 38 ms, faster than 32.55%
        Memory Usage: 14.2 MB, less than 55.31%

        1 <= pattern.length <= 300
        pattern contains only lower-case English letters.
        1 <= s.length <= 3000
        s contains only lowercase English letters and spaces ' '.
        s does not contain any leading or trailing spaces.
        All the words in s are separated by a single space.
        :param pattern:
        :param s:
        :return:
        """
        values = s.split()
        if len(pattern) != len(values):
            return False
        d = dict()
        d2 = dict()
        for i in range(len(pattern)):
            p = pattern[i]
            v = values[i]
            if p in d and v != d.get(p):
                return False
            elif p not in d:
                d[p] = v

            if v in d2 and p != d2.get(v):
                return False
            elif v not in d2:
                d2[v] = p

        return True


def test():
    assert Solution().wordPattern(pattern="abba", s="dog cat cat dog")
    assert not Solution().wordPattern(pattern="abba", s="dog dog dog dog")
    assert not Solution().wordPattern(pattern="abba", s="dog cat cat fish")
    assert not Solution().wordPattern(pattern="aaaa", s="dog cat cat dog")


if __name__ == '__main__':
    test()
