#!/usr/bin/env python
"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Created on 2018-12-28

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""

num_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ret = ['']
        for d in digits:
            tmp_ret = []
            for r in ret:
                for l in num_dict[d]:
                    tmp_ret.append(r + l)
            ret = tmp_ret
        return ret


if __name__ == '__main__':
    print(Solution().letterCombinations('235'))
    assert set(Solution().letterCombinations('23')) == {'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'}
    assert Solution().letterCombinations('') == []
