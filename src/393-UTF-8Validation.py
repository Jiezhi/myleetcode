#!/usr/bin/env python3
"""
CREATED AT: 2022-09-13

URL: https://leetcode.com/problems/utf-8-validation/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 393-UTF-8Validation

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        Runtime: 145 ms, faster than 77.92%
        Memory Usage: 14.1 MB, less than 70.76%

        1 <= data.length <= 2 * 10^4
        0 <= data[i] <= 255
        """
        i, n = 0, len(data)
        transform = lambda x: format(x, 'b').zfill(8)
        while i < n:
            binary = transform(data[i])
            if binary.startswith('0'):
                i += 1
                continue
            elif binary.startswith('110'):
                if i + 1 >= n or not transform(data[i + 1]).startswith('10'):
                    return False
                i += 2
            elif binary.startswith('1110'):
                if i + 2 >= n or not (
                        transform(data[i + 1]).startswith('10') and transform(data[i + 2]).startswith('10')):
                    return False
                i += 3
            elif binary.startswith('11110'):
                if i + 3 >= n or not (transform(data[i + 1]).startswith('10') and transform(data[i + 2]).startswith(
                        '10') and transform(data[i + 3]).startswith('10')):
                    return False
                i += 4
            else:
                return False
        return True


def test():
    assert Solution().validUtf8(data=[197, 130, 1])
    assert not Solution().validUtf8(data=[235, 140, 4])


if __name__ == '__main__':
    test()
