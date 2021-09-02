#!/usr/bin/env python
"""
CREATED AT: 2021/9/2
Des:
https://leetcode.com/problems/search-in-a-binary-search-tree/
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1000/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        36 / 36 test cases passed.
        Status: Accepted
        Runtime: 89 ms
        Memory Usage: 16.1 MB
        :param root:
        :param val:
        :return:
        """
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


def test():
    assert Solution().searchBST(root=build_tree_node([4, 2, 7, 1, 3]), val=2) == build_tree_node([2, 1, 3])


if __name__ == '__main__':
    test()
