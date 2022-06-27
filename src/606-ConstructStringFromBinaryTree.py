#!/usr/bin/env python
"""
CREATED AT: 2022/3/19
Des:

https://leetcode.com/problems/construct-string-from-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        The number of nodes in the tree is in the range [1, 10^4].
        -1000 <= Node.val <= 1000

        Runtime: 52 ms, faster than 90.58%
        Memory Usage: 16.3 MB, less than 65.08%

        :param root:
        :return:
        """
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return f'{root.val}({self.tree2str(root.left)})'
        return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'


def test():
    assert Solution().tree2str(build_tree_node([1, 2, 3, 4])) == "1(2(4))(3)"
    assert Solution().tree2str(build_tree_node([1, 2, 3, None, 4])) == "1(2()(4))(3)"


if __name__ == '__main__':
    test()
