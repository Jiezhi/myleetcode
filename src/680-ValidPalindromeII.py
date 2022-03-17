#!/usr/bin/env python
"""
CREATED AT: 2022/3/17
Des:

https://leetcode.com/problems/valid-palindrome-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Runtime: 300 ms, faster than 18.37%
        Memory Usage: 14.6 MB, less than 24.42%

        1 <= s.length <= 10^5
        s consists of lowercase English letters.
        """

        def isPalindrome(s: str) -> int:
            lo, hi = 0, len(s) - 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return lo
                lo += 1
                hi -= 1
            return -1

        lo = isPalindrome(s)
        hi = len(s) - lo

        if lo == -1:
            return True

        return isPalindrome(s[lo: hi - 1]) == -1 or isPalindrome(s[lo + 1: hi]) == -1


def test():
    assert Solution().validPalindrome("aba") == True
    assert Solution().validPalindrome("abca") == True
    assert Solution().validPalindrome("abcc") == False


if __name__ == '__main__':
    test()
