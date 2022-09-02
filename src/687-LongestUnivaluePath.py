#!/usr/bin/env python3
"""
CREATED AT: 2022-09-02

URL: https://leetcode.com/problems/longest-univalue-path/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 687-LongestUnivaluePath

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 737 ms, faster than 19.06%
        Memory Usage: 18.1 MB, less than 8.06%

        The number of nodes in the tree is in the range [0, 10^4].
        -1000 <= Node.val <= 1000
        The depth of the tree will not exceed 1000.
        """

        def getMaxPath(node) -> (int, int):
            """
            return the max path, root node as edge node or not
            """
            if not node:
                return 0, 0
            ret1, ret2 = 0, 0
            if node.left:
                l1, l2 = getMaxPath(node.left)
                if node.val == node.left.val:
                    ret1 = max(ret1, l1 + 1)
                ret2 = max(ret2, l2)

            if node.right:
                r1, r2 = getMaxPath(node.right)
                if node.val == node.right.val:
                    ret1 = max(ret1, r1 + 1)
                    if node.left and node.val == node.left.val:
                        # node.val == node.left.val == node.right.val
                        ret2 = max(ret2, l1 + r1 + 2)
                ret2 = max(ret2, r2)
            return ret1, max(ret1, ret2)

        _, ret = getMaxPath(root)
        return ret


def test():
    assert Solution().longestUnivaluePath(root=TreeNode.from_list([1, 2, 1])) == 1
    assert Solution().longestUnivaluePath(root=TreeNode.from_list([1, 2, 3, 4, 2])) == 1
    assert Solution().longestUnivaluePath(root=TreeNode.from_list([5, 4, 5, 1, 1, null, 5])) == 2
    assert Solution().longestUnivaluePath(root=TreeNode.from_list([1, 4, 5, 4, 4, null, 5])) == 2


if __name__ == '__main__':
    test()
