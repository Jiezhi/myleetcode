#!/usr/bin/env python
"""
https://leetcode.com/problems/add-binary/description/
Created on 2018-11-15

@author: 'Jiezhi.G@gmail.com'

Make a/b to a int, then add them and turn the result to binary format

Reference: 
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2))[2:])


if __name__ == '__main__':
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary("1010", "1011") == "10101"
