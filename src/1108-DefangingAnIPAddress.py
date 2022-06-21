#!/usr/bin/env python3
"""
CREATED AT: 2022-06-21

URL: https://leetcode.com/problems/defanging-an-ip-address/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1108-DefangingAnIPAddress

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Runtime: 72 ms, faster than 5.35%
        Memory Usage: 13.9 MB, less than 6.02%
        :param address: The given address is a valid IPv4 address.
        :return:
        """
        return address.replace('.', '[.]')


def test():
    assert Solution().defangIPaddr(address="1.1.1.1") == "1[.]1[.]1[.]1"


if __name__ == '__main__':
    test()
