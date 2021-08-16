#!/usr/bin/env python
"""
CREATED AT: 2021/8/16
Des:
https://leetcode.com/problems/valid-palindrome/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        480 / 480 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.6 MB
        :param s:
        :return:
        """
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True


def test():
    assert Solution().isPalindrome(s="A man, a plan, a canal: Panama")
    assert not Solution().isPalindrome(s="race a car")


if __name__ == '__main__':
    test()
