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

    def __repr__(self):
        ret = []
        node = self
        while node is not None:
            ret.append(node.val)
            node = node.next
        return str(ret)


def buildListNode(nums):
    ret = tmp = ListNode(0)
    for num in nums:
        tmp.next = ListNode(num)
        tmp = tmp.next
    return ret.next


def buildCycleList(nums, pos):
    if pos == -1:
        return buildListNode(nums)
    if pos >= len(nums):
        return None
    ret = tmp = ListNode(0)
    for i in range(len(nums)):
        tmp.next = ListNode(nums[i])
        tmp = tmp.next
        if i == pos:
            cycle_entry = tmp
    tmp.next = cycle_entry
    return ret.next


def printData(l):
    while l:
        print(l.val)
        l = l.next
    print('----')


if __name__ == '__main__':
    assert buildListNode([1, 2]) == buildListNode([1, 2])
    ret = buildCycleList([0, 1, 2, 3, 4], 0)
    assert ret.val == 0
