#!/usr/bin/env python
"""
CREATED AT: 2021/8/30
Des:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import node
from node import Node
from tool import print_results


class Solution:
    @print_results
    def connect(self, root: Node) -> Node:
        """
        58 / 58 test cases passed.
        Status: Accepted
        Runtime: 56 ms
        Memory Usage: 15.7 MB
        :param root:
        :return:
        """
        if root is None or root.val is None:
            return root
        parent_list = [root, None]
        child_list = []
        while len(parent_list) > 1:
            for i in range(len(parent_list) - 1):
                parent_list[i].next = parent_list[i + 1]
                if parent_list[i].left is not None:
                    child_list.append(parent_list[i].left)
                if parent_list[i].right is not None:
                    child_list.append(parent_list[i].right)

            parent_list = child_list.copy()
            parent_list.append(None)
            child_list = []
        return root


def test():
    assert Solution().connect(root=node.build_node_without_next([1, 2, 3, 4, 5, 6, 7]))


if __name__ == '__main__':
    test()
