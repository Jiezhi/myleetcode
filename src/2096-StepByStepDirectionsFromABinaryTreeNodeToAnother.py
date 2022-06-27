#!/usr/bin/env python
"""
CREATED AT: 2021/12/5
Des:

https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another
https://leetcode.com/contest/weekly-contest-270/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
import collections
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        The number of nodes in the tree is n.
        2 <= n <= 10^5
        1 <= Node.val <= n
        All the values in the tree are unique.
        1 <= startValue, destValue <= n
        startValue != destValue
        :param root:
        :param startValue:
        :param destValue:
        :return:
        """
        if root is None:
            return ""

        dq = collections.deque()
        dq.append((root, ""))
        start_found = False
        dest_found = False
        start_path = ""
        dest_path = ""
        while len(dq) > 0 and not (start_found and dest_found):
            node, path = dq.popleft()
            if node.val == startValue:
                start_found = True
                start_path = path
            elif node.val == destValue:
                dest_found = True
                dest_path = path
            if node.left is not None:
                dq.append((node.left, path + "L"))
            if node.right is not None:
                dq.append((node.right, path + "R"))
        i = 0
        while len(start_path) > i and len(dest_path) > i and start_path[i] == dest_path[i]:
            i += 1
        return (len(start_path) - i) * 'U' + dest_path[i:]


def test():
    null = None
    assert Solution().getDirections(root=build_tree_node([5, 1, 2, 3, null, 6, 4]), startValue=3, destValue=6) == "UURL"
    assert Solution().getDirections(root=build_tree_node([2, 1]), startValue=2, destValue=1) == "L"


if __name__ == '__main__':
    test()
