#!/usr/bin/env python
"""
CREATED AT: 2022/3/9
Des:

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from src.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Runtime: 62 ms, faster than 43.38%
        Memory Usage: 14 MB, less than 35.01%

        The number of nodes in the list is in the range [0, 300].
        -100 <= Node.val <= 100
        The list is guaranteed to be sorted in ascending order.
        """
        if not head or not head.next:
            return head
        # remove duplicates of the head
        dup = False
        while head and head.next:
            if head.val == head.next.val:
                dup = True
                head = head.next
            else:
                break
        if dup:
            head = head.next
            return self.deleteDuplicates(head)
        p_node = head
        node = p_node.next
        dup = False
        while node and node.next:
            if node.val == node.next.val:
                dup = True
                node.next = node.next.next
            else:
                if dup:
                    p_node.next = node.next
                    dup = False
                else:
                    p_node = node
                node = node.next
        if dup:
            p_node.next = node.next
        return head


def test():
    assert Solution().deleteDuplicates(ListNode.from_list([1, 2, 3, 3, 4, 4, 5])) == ListNode.from_list([1, 2, 5])
    assert Solution().deleteDuplicates(ListNode.from_list([1, 1, 1, 2, 3])) == ListNode.from_list([2, 3])


if __name__ == '__main__':
    test()
