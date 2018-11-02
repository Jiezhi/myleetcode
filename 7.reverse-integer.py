"""
 https://leetcode.com/problems/reverse-integer/description/
 @Author: Jiezhi 
 @Date: 2018-11-02 16:13:53 
 @Last Modified by:   Jiezhi 
 @Last Modified time: 2018-11-02 16:13:53 
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        l = len(s)
        ret = ''
        if s[0] == '-':
            ret += '-'
            l -= 1
        
        for i in range(l):
            ret += s[-i - 1]
        x = int(ret)
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        return x

if __name__ == '__main__':
    print(Solution().reverse(-1024))