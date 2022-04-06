#!/usr/bin/env python
"""
CREATED AT: 2022/4/6
Des:

https://leetcode.com/problems/binary-tree-right-side-view/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""

from typing import Optional, List

from src.tree_node import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Runtime: 74 ms, faster than 5.20%
        Memory Usage: 13.8 MB, less than 75.55%

        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100
        """
        if not root:
            return []
        ret = []
        cur_level = [root]
        while cur_level:
            next_level = []
            ret.append(cur_level[-1].val)
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
        return ret


def test():
    assert Solution().rightSideView(TreeNode.from_list([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert Solution().rightSideView(TreeNode.from_list([1, None, 3])) == [1, 3]
    assert Solution().rightSideView(TreeNode.from_list([])) == []


if __name__ == '__main__':
    test()
