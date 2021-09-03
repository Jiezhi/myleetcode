#!/usr/bin/env python
"""
CREATED AT: 2021/9/2
Des:
https://leetcode.com/problems/insert-into-a-binary-search-tree/
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1003/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import Optional

from tool import print_results
from tree_node import TreeNode, build_tree_node


class Solution:
    @print_results
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        35 / 35 test cases passed.
        Status: Accepted
        Runtime: 139 ms
        Memory Usage: 16.7 MB
        :param root:
        :param val:
        :return:
        """
        insert_node = TreeNode(val)
        if root is None:
            return insert_node
        node = root
        while True:
            if node.val > val:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = insert_node
                    return root
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = insert_node
                    return root


def test():
    assert Solution().insertIntoBST(root=build_tree_node([4, 2, 7, 1, 3]), val=5)
    assert Solution().insertIntoBST(root=build_tree_node([40, 20, 60, 10, 30, 50, 70]), val=25)


if __name__ == '__main__':
    test()
