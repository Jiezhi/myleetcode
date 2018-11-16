#!/usr/bin/env python
"""
Created on 2018-11-16

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next
        if not self and not other:
            return True
        else:
            return False


def buildListNode(nums):
    ret = tmp = ListNode(0)
    for num in nums:
        tmp.next = ListNode(num)
        tmp = tmp.next
    return ret.next


def printData(l):
    while l:
        print(l.val)
        l = l.next
    print('----')


if __name__ == '__main__':
    print(buildListNode([1, 2]) == buildListNode([1, 2]))
