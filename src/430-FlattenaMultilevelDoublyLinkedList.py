#!/usr/bin/env python
"""
CREATED AT: 2021/12/06
Des:

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """
        26 / 26 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 15.1 MB
        The number of Nodes will not exceed 1000.
        1 <= Node.val <= 10^5
        :param head:
        :return:
        """

        def sub_flatten(head: 'Node') -> ('Node', 'Node'):
            node = head
            pre_tail = node
            while node is not None:
                pre_tail = node
                if node.child is not None:
                    chead, ctail = sub_flatten(node.child)
                    if node.next is not None:
                        ctail.next = node.next
                        node.next.prev = ctail
                    node.next = chead
                    chead.prev = node
                    node.child = None
                    node = ctail
                else:
                    node = node.next
            return head, pre_tail

        sub_flatten(head)
        return head


def test():
    # TODO build example node
    #  1---2---3---4---5---6--NULL
    #          |
    #          7---8---9---10--NULL
    #              |
    #              11--12--NULL
    pass


if __name__ == '__main__':
    test()
