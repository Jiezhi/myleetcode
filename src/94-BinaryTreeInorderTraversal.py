#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-25

Leetcode: https://leetcode.com/problems/binary-tree-inorder-traversal/

Same as: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

"""
from typing import Optional

from tree_node import *


class Solution:
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """
        Update on 2022/04/19
        Morris Traversal O(1) space
        Runtime: 50 ms, faster than 30.13%
        Memory Usage: 13.9 MB, less than 62.62%

        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100
        """
        ret = []
        cur = root
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if cur == tmp.right:
                    tmp.right = None
                    ret.append(cur.val)
                    cur = cur.right
                # Blow commented code would skip operation when cur node's left child is a leaf node.
                # elif cur.left == tmp:
                #     ret.append(cur.left.val)
                #     ret.append(cur.val)
                #     cur = cur.right
                else:
                    tmp.right = cur
                    cur = cur.left

        return ret

    # Recursive solution could be found at explore/data_structure_tree/inorder_traversal.py
    def inorderTraversal(self, root: TreeNode) -> list:
        ret = []
        if not root:
            return ret
        stack = []
        tmp = root
        while tmp or len(stack) > 0:
            if tmp:
                stack.append(tmp)
                tmp = tmp.left
            else:
                tmp = stack.pop()
                ret.append(tmp.val)
                tmp = tmp.right
        return ret


def test():
    assert Solution().inorderTraversal(build_tree_node([1, None, 2, 3])) == [1, 3, 2]
    assert Solution().inorderTraversal2(build_tree_node([1, None, 2, 3])) == [1, 3, 2]


if __name__ == '__main__':
    test()
