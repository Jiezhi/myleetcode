#!/usr/bin/env python
"""
CREATED AT: 2021/10/17
Des:
https://leetcode.com/problems/path-sum-iii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: Tree

See: 
"""

from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Runtime: 300 ms, faster than 40.18%
        Memory Usage: 35.1 MB, less than 5.93%
        The number of nodes in the tree is in the range [0, 1000].
        -10**9 <= Node.val <= 10**9
        -1000 <= targetSum <= 1000
        :param root:
        :param targetSum:
        :return:
        """
        ret = 0

        def dfs(tree: TreeNode, parent_list):
            """
            we keep track every sum situation
            :param tree:
            :param parent_list:
            :return:
            """
            nonlocal ret
            if tree is None:
                return
            cur_list = [x + tree.val for x in parent_list]
            cur_list.append(tree.val)
            for num in cur_list:
                if num == targetSum:
                    ret += 1
            dfs(tree.left, cur_list)
            dfs(tree.right, cur_list)

        dfs(root, [])
        return ret


def test():
    null = None
    assert Solution().pathSum(build_tree_node([0, 1, 1]), 1) == 4
    assert Solution().pathSum(
        root=build_tree_node([10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]),
        targetSum=8) == 3
    assert Solution().pathSum(
        root=build_tree_node([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 11]),
        targetSum=22) == 3


if __name__ == '__main__':
    test()
