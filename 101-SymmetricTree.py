#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-04-24

Leetcode: https://leetcode.com/problems/symmetric-tree/

See also: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/

"""
from tree_node import *


class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return self.sameChild(root.left, root.right)

    def sameChild(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.sameChild(left.left, right.right) and self.sameChild(left.right, right.left)


def test():
    assert Solution().isSymmetric(build_tree_node([1, 2, 2, 3, 4, 4, 3]))
    assert not Solution().isSymmetric(build_tree_node([1, 2, 2, 2, None, 2]))
    assert not Solution().isSymmetric(build_tree_node([1, 2, 3]))
    assert not Solution().isSymmetric(build_tree_node([5, 4, 1, None, 1, None, 4, 2, None, 2, None]))
    assert not Solution().isSymmetric(build_tree_node([1, 2, 2, None, 3, None, 3]))


if __name__ == '__main__':
    test()
