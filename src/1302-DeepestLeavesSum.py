#!/usr/bin/env python
"""
CREATED AT: 2022/5/15
Des:
https://leetcode.com/problems/deepest-leaves-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import Optional
from tree_node import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        AC: 05/15/2022 17:32
        Runtime: 281 ms, faster than 53.41%
        Memory Usage: 17.7 MB, less than 66.46%
        :param root: The number of nodes in the tree is in the range [1, 104].
        1 <= Node.val <= 100
        :return:
        """
        cur_level = [root]
        while cur_level:
            pre_level = cur_level
            cur_level = []
            for node in pre_level:
                if node.left or node.right:
                    if node.left:
                        cur_level.append(node.left)
                    if node.right:
                        cur_level.append(node.right)
        return sum(x.val for x in pre_level)


def test():
    null = None
    assert Solution().deepestLeavesSum(
        root=TreeNode.from_list([1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8])) == 15


if __name__ == '__main__':
    test()
