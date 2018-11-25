#!/usr/bin/env python
"""
https://leetcode.com/problems/zigzag-conversion/description/
Created on 2018-11-25

@author: 'Jiezhi.G@gmail.com'

Reference:
"""


class Solution:
    def convert(self, s, numRows):
        """
        he first line and last line are Arithmetic progression（等差数列）
        The regular of those lines between first and last is like(when numRows=6):
        10 10 10 10..
        8 2 8 2 8 2.. (8 + 2 = 10)
        6 4 6 4 6 4.. (6 + 4 = 10)
        4 6 4 6 4 6.. (4 + 6 = 10)
        2 8 2 8 2 8.. (2 + 8 = 10)
        10 10 10 10 ..

        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        max_step = 2 * numRows - 2

        s2 = s[0:len(s): max_step]
        for i in range(1, numRows - 1):
            j = i
            step = (numRows - i - 1) * 2
            while j < len(s):
                s2 += s[j]
                j += step
                step = max_step - step
        s2 += s[numRows - 1:len(s): max_step]
        return s2


if __name__ == '__main__':
    assert Solution().convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
