#!/usr/bin/env python
"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
Created on 2018-11-11

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = l3 = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return ret.next


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
    t = buildListNode([1, 2, 3])
    printData(t)
    printData(Solution().mergeTwoLists(buildListNode([1, 2, 3]), buildListNode([2, 3, 4])))
