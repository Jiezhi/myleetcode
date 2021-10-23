#!/usr/bin/env python
"""
CREATED AT: 2021/8/17
Des:
https://leetcode.com/problems/validate-binary-search-tree/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/625/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

from typing import Optional

import tree_node
from tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        80 / 80 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 17.3 MB
        :param root:
        :return:
        """

        def dfs(sub_tree: TreeNode):
            """
            return the sub tree's min and max valuse and compare them with parent val
            left subtree's maximum value should less than the val,
            and the right subtree's minimum value should greater than the val
            :param sub_tree:
            :return:
            """
            if not sub_tree.left and not sub_tree.right:
                return sub_tree.val, sub_tree.val, True
            min_value = sub_tree.val
            max_value = sub_tree.val
            if sub_tree.left:
                tmp_left_min_value, tmp_left_max_value, valid = dfs(sub_tree.left)
                if not valid or tmp_left_max_value >= sub_tree.val:
                    return tmp_left_min_value, tmp_left_max_value, False
                if tmp_left_min_value:
                    min_value = min(min_value, tmp_left_min_value)
            if sub_tree.right:
                tmp_right_min_value, tmp_right_max_value, valid = dfs(sub_tree.right)
                if not valid or (tmp_right_min_value <= sub_tree.val):
                    return tmp_right_min_value, tmp_right_max_value, False
                if tmp_right_max_value:
                    max_value = max(max_value, tmp_right_max_value)
            return min_value, max_value, True

        _, _, isvalid = dfs(root)
        return isvalid


def test():
    null = None
    assert Solution().isValidBST(root=tree_node.build_tree_node([2, 1, 3]))
    assert not Solution().isValidBST(root=tree_node.build_tree_node([5, 1, 4, null, null, 3, 6]))
    assert not Solution().isValidBST(root=tree_node.build_tree_node([2, 2, 2]))
    assert not Solution().isValidBST(root=tree_node.build_tree_node([5, 4, 6, null, null, 3, 7]))


if __name__ == '__main__':
    test()
