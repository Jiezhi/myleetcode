#!/usr/bin/env python
"""
Created on 2018-11-06

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        for i in range(int(len(x) / 2)):
            if x[i] != x[-i - 1]:
                return False
        return True


if __name__ == '__main__':
    assert Solution().isPalindrome(121) is True
    assert Solution().isPalindrome(-121) is False
    assert Solution().isPalindrome(10) is False
