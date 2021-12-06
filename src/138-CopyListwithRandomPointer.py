#!/usr/bin/env python
"""
CREATED AT: 2021/12/06
Des:

https://leetcode.com/problems/copy-list-with-random-pointer/
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Finished by Hint 3
        Runtime: 28 ms, faster than 97.12%
        Memory Usage: 14.9 MB, less than 63.37%
        0 <= n <= 1000
        -10000 <= Node.val <= 10000
        Node.random is null or is pointing to some node in the linked list.
        :param head:
        :return:
        """
        if head is None:
            return None
        node = head
        # insert every node copy into original nodes gap.
        while node is not None:
            tmp_node = Node(node.val, next=node.next)
            node.next = tmp_node
            node = tmp_node.next
        # copy every original node random pointers
        node = head
        while node is not None:
            if node.random is not None:
                node.next.random = node.random.next
            node = node.next.next
        # remove the original nodes
        node = head.next
        while node.next is not None:
            node.next = node.next.next
            node = node.next
        return head.next


def test():
    assert Solution().copyRandomList(head=Node(0)).val == 0


if __name__ == '__main__':
    test()
