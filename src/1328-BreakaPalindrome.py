#!/usr/bin/env python
"""
CREATED AT: 2021/9/23
Des:

https://leetcode.com/problems/break-a-palindrome
https://leetcode.com/explore/item/3985
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        30 / 30 test cases passed.
        Status: Accepted
        Runtime: 28 ms
        Memory Usage: 14.3 MB
        :param palindrome:
        :return:
        """
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]

        return palindrome[:-1] + 'b'


def test():
    assert Solution().breakPalindrome(palindrome="abccba") == "aaccba"
    assert Solution().breakPalindrome(palindrome="a") == ""
    assert Solution().breakPalindrome(palindrome="aa") == "ab"
    assert Solution().breakPalindrome(palindrome="aba") == "abb"


if __name__ == '__main__':
    test()
