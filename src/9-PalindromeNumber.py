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
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        # Solution 1:
        # Noticed that can't use str()
        # x = str(x)
        # for i in range(int(len(x) / 2)):
        #     if x[i] != x[-i - 1]:
        #         return False
        # return True

        # Solution 2:
        # get the len of number first
        # l = 0
        # tmp = x
        # while tmp > 0:
        #     l += 1
        #     tmp = tmp // 10
        # for i in range(1, int(l / 2) + 1):
        #     if get_int_pos(x, l, i) != get_int_pos(x, l, l - i + 1):
        #         return False
        # return True

        # solution 3:
        ret = 0
        while x > ret:
            ret = ret * 10 + x % 10
            x = x // 10
        return x == ret or x == ret // 10


def get_int_pos(x, l, i):
    """
    index from base 1
    :param x:
    :param l:
    :param i:
    :return:
    """
    return x % (10 ** (l - i + 1)) // 10 ** (l - i)


def test():
    assert get_int_pos(121, 3, 2) == 2
    assert get_int_pos(1234567, 7, 4) == 4
    assert Solution().isPalindrome(8) is True
    assert Solution().isPalindrome(121) is True
    assert Solution().isPalindrome(-121) is False
    assert Solution().isPalindrome(10) is False
    assert get_int_pos(5555, 4, 2) == 5
    assert Solution().isPalindrome(5555) is True
