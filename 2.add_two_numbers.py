"""
https://leetcode.com/problems/add-two-numbers
 @Author: Jiezhi.G@gmail.com
 @Date: 2018-07-06 17:43:26 
 @Last Modified by:   Jiezhi 
 @Last Modified time: 2018-07-06 17:43:26 
"""

from list_node import *


class Solution:
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add_one = False
        l3 = tmp = ListNode(0)
        while l1 or l2:
            result = 0
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            if add_one:
                result += 1
                add_one = False
            if result > 9:
                add_one = True
            tmp.next = ListNode(result % 10)
            tmp = tmp.next
        if add_one:
            tmp.next = ListNode(1)
        return l3.next


if __name__ == '__main__':
    assert Solution().add_two_numbers(
        buildListNode([2, 4, 3]),
        buildListNode([5, 6, 4])
    ) == buildListNode([7, 0, 8])
