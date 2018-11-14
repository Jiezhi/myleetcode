#!/usr/bin/env python
"""
https://leetcode.com/problems/plus-one/description/
Created on 2018-11-14

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) - 1
        while l >= 0 and digits[l] == 9:
            digits[l] = 0
            l -= 1
        if l < 0:
            digits.insert(0, 1)
        else:
            digits[l] += 1
        return digits


if __name__ == '__main__':
    assert Solution().plusOne([0]) == [1]
    assert Solution().plusOne([1, 2, 3, 4]) == [1, 2, 3, 5]
    assert Solution().plusOne([1, 2, 3, 9]) == [1, 2, 4, 0]
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0]
