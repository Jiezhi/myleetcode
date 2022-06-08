#!/usr/bin/env python3
"""
CREATED AT: 2022-06-08
Des: https://leetcode.com/problems/remove-palindromic-subsequences/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
        Runtime: 43 ms, faster than 40.61%
        Memory Usage: 13.9 MB, less than 53.87%

        Actually, if the s is palindrome, the answer is 1 else 2
        There only two chars a or b, we can take all 'a' then all 'b' in two steps.
        
        1 <= s.length <= 1000
        s[i] is either 'a' or 'b'.
        """

        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        return 1 if isPalindrome(s) else 2


def test():
    assert Solution().removePalindromeSub(s="ababa") == 1
    assert Solution().removePalindromeSub(s="aab") == 2
    assert Solution().removePalindromeSub(s="baabb") == 2


if __name__ == '__main__':
    test()
