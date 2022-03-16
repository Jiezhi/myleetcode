#!/usr/bin/env python
"""
CREATED AT: 2022/3/16
Des:

https://leetcode.com/problems/reverse-vowels-of-a-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Runtime: 70 ms, faster than 68.55%
        Memory Usage: 15 MB, less than 64.49%

        1 <= s.length <= 3 * 10^5
        s consist of printable ASCII characters.
        """
        lo, hi = 0, len(s) - 1
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while lo < hi:
            while lo < hi and s[lo] not in vowels:
                lo += 1
            while lo < hi and s[hi] not in vowels:
                hi -= 1
            if lo < hi:
                s[lo], s[hi] = s[hi], s[lo]
                lo += 1
                hi -= 1
        return ''.join(s)


def test():
    assert Solution().reverseVowels("hello") == "holle"
    assert Solution().reverseVowels("leetcode") == "leotcede"
    assert Solution().reverseVowels("aA") == "Aa"


if __name__ == '__main__':
    test()
