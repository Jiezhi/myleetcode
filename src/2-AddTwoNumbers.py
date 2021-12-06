"""
https://leetcode.com/problems/add-two-numbers
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/

 @Author: Jiezhi.G@gmail.com
 @Date: 2018-07-06 17:43:26 
 @Last Modified by:   Jiezhi 
 @Last Modified time: 2021-12-06
"""
from typing import Optional

from list_node import *


class Solution:
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Updated at 2021-12-06
        1568 / 1568 test cases passed.
        Runtime: 68 ms, faster than 77.74%
        Memory Usage: 14.2 MB, less than 91.26%
        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.
        :param l1:
        :param l2:
        :return:
        """
        node1, node2 = l1, l2
        flag = 0
        while node1 is not None or node2 is not None or flag > 0:
            if node1 is None and node2 is None:
                last_node1.next = ListNode(flag)
                break
            if node1 is None:
                node1 = node2
                last_node1.next = node1
                node2 = None
            node2val = node2.val if node2 is not None else 0
            ret = flag + node1.val + node2val
            flag, node1.val = divmod(ret, 10)
            last_node1 = node1
            node1 = node1.next
            if node2 is not None:
                node2 = node2.next

        return l1

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


def test():
    assert Solution().add_two_numbers(
        buildListNode([2, 4, 3]),
        buildListNode([5, 6, 4])
    ) == buildListNode([7, 0, 8])

    assert Solution().addTwoNumbers2(
        l1=buildListNode([2, 4, 3]),
        l2=buildListNode([5, 6, 4])
    ) == buildListNode([7, 0, 8])

    assert Solution().addTwoNumbers2(
        l1=buildListNode([0]),
        l2=buildListNode([0])
    ) == buildListNode([0])

    assert Solution().addTwoNumbers2(
        l1=buildListNode([9, 9, 9, 9, 9, 9, 9]),
        l2=buildListNode([9, 9, 9, 9])
    ) == buildListNode([8, 9, 9, 9, 0, 0, 0, 1])

    assert Solution().addTwoNumbers2(
        l1=buildListNode([5]),
        l2=buildListNode([5])
    ) == buildListNode([0, 1])

    assert Solution().addTwoNumbers2(
        l1=buildListNode([0]),
        l2=buildListNode([1])
    ) == buildListNode([1])

    assert Solution().addTwoNumbers2(
        l1=buildListNode([9, 9, 9, 9, 9, 9, 9]),
        l2=buildListNode([1])
    ) == buildListNode([0, 0, 0, 0, 0, 0, 0, 1])

    assert Solution().addTwoNumbers2(
        l2=buildListNode([9, 9, 9, 9, 9, 9, 9]),
        l1=buildListNode([1])
    ) == buildListNode([0, 0, 0, 0, 0, 0, 0, 1])


if __name__ == '__main__':
    test()
