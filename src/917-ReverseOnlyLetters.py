#!/usr/bin/env python
"""
CREATED AT: 2021/9/14
Des:
https://leetcode.com/problems/reverse-only-letters
https://leetcode.com/explore/item/3974
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from tool import print_results


class Solution:
    @print_results
    def reverseOnlyLetters(self, s: str) -> str:
        """
        115 / 115 test cases passed.
        Status: Accepted
        Runtime: 73 ms
        Memory Usage: 14.1 MB
        :param s:
        :return:
        """
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalpha() and i < j:
                i += 1
            while not s[j].isalpha() and i < j:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)


def test():
    assert Solution().reverseOnlyLetters(s="ab-cd") == "dc-ba"
    assert Solution().reverseOnlyLetters(s="a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert Solution().reverseOnlyLetters(s="Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"


if __name__ == '__main__':
    test()
