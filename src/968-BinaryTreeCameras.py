#!/usr/bin/env python3
"""
CREATED AT: 2022-06-17

URL: https://leetcode.com/problems/binary-tree-cameras/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 968-BinaryTreeCameras

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
import math
from typing import Optional

from tree_node import TreeNode


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        Ref: https://leetcode.com/problems/binary-tree-cameras/solution/
        Runtime: 69 ms, faster than 45.51%
        Memory Usage: 14.3 MB, less than 21.59%
        The number of nodes in the tree is in the range [1, 1000].
        Node.val == 0
        """

        def dfs(node) -> (int, int, int):
            if not node:
                return 0, 0, math.inf
            lc, rc = dfs(node.left), dfs(node.right)
            dp0 = lc[1] + rc[1]
            dp1 = min(lc[2] + min(rc[1], rc[2]), rc[2] + min(lc[1], lc[2]))
            dp2 = 1 + min(lc) + min(rc)

            return dp0, dp1, dp2

        ret = dfs(root)
        return min(ret[1], ret[2])


def test():
    null = None
    assert Solution().minCameraCover(TreeNode.from_list([0, 0, null, 0, 0])) == 1
    assert Solution().minCameraCover(TreeNode.from_list([0, 0, null, 0, null, 0, null, null, 0])) == 2


if __name__ == '__main__':
    test()
