#!/usr/bin/env python
"""
CREATED AT: 2021/11/22
Des:

https://leetcode.com/problems/delete-node-in-a-bst/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: BST

See: 
"""
from typing import Optional

from src.tree_node import TreeNode, build_tree_node


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Runtime: 76 ms, faster than 63.07%
        Memory Usage: 18.5 MB, less than 22.29%

        The number of nodes in the tree is in the range [0, 10^4].
        -10^5 <= Node.val <= 10^5
        Each node has a unique value.
        root is a valid binary search tree.
        -10^5 <= key <= 10^5

        :param root:
        :param key:
        :return:
        """
        if root is None:
            return root

        # if not found key in BST, just return root
        # if found, noted as keynode, and we need replace this node
        # by the maximum node in its left side or minimum node in its right side.
        def replace(node):
            if node is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # we choose left maximum node to be the root node
            parent_node = node
            tmp_node = parent_node.left
            if tmp_node.right is None:
                tmp_node.right = node.right
                return tmp_node
            while tmp_node.right is not None:
                parent_node = tmp_node
                tmp_node = tmp_node.right
            parent_node.right = tmp_node.left
            tmp_node.left = node.left
            tmp_node.right = node.right
            return tmp_node

        if root.val == key:
            return replace(root)
        p_node = root
        while p_node is not None:
            if p_node.left and key == p_node.left.val:
                p_node.left = replace(p_node.left)
                return root
            if p_node.right and key == p_node.right.val:
                p_node.right = replace(p_node.right)
                return root
            if key < p_node.val:
                p_node = p_node.left
            else:
                p_node = p_node.right
        return root


def test():
    null = None
    tree_list = [22, 19, 24, 17, 21, 23, null, 16, 18, 20]
    root = build_tree_node(tree_list)
    ret_list = [21, 19, 24, 17, 20, 23, null, 16, 18]
    assert Solution().deleteNode(root=root, key=22) == build_tree_node(ret_list)
    # Delete root node
    ret = Solution().deleteNode(root=build_tree_node([2, 1, 3]), key=2)
    assert ret == build_tree_node([1, null, 3]) or ret == build_tree_node([3, 1])

    assert Solution().deleteNode(root=build_tree_node([2, 1, 3]), key=1) == build_tree_node([2, null, 3])
    assert Solution().deleteNode(root=build_tree_node([2, 1, 3]), key=3) == build_tree_node([2, 1])
    assert Solution().deleteNode(root=build_tree_node([2, 1, 3]), key=4) == build_tree_node([2, 1, 3])

    ret = Solution().deleteNode(root=build_tree_node([5, 3, 6, 2, 4, null, 7]), key=3)

    assert ret == build_tree_node([5, 4, 6, 2, null, null, 7]) or ret == build_tree_node([5, 2, 6, null, 4, null, 7])
    assert Solution().deleteNode(root=build_tree_node([5, 3, 6, 2, 4, null, 7]), key=0) == \
           build_tree_node([5, 3, 6, 2, 4, null, 7])
    assert Solution().deleteNode(root=build_tree_node([]), key=0) == build_tree_node([])


if __name__ == '__main__':
    test()
