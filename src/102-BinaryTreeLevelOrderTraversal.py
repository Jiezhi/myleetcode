#!/usr/bin/env python
"""
URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-26

Difficulty: Medium

Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/

See also: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

"""
import collections
import queue
from typing import Optional

from tree_node import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime: 57 ms, faster than 42.29% 
        Memory Usage: 14.2 MB, less than 84.23% 

        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000
        """
        if not root:
            return []
        ret, tmp = [], []
        pre_level = 0
        dq = collections.deque([(root, 0)])
        while dq:
            node, level = dq.popleft()
            if level > pre_level:
                ret.append(tmp)
                tmp = []
                pre_level = level
            tmp.append(node.val)
            if node.left:
                dq.append((node.left, level + 1))
            if node.right:
                dq.append((node.right, level + 1))
        if tmp:
            ret.append(tmp)
        return ret

    def level_order(self, root: TreeNode) -> list:
        if not root:
            return []
        ret = []
        q = queue.Queue()
        q.put([root])
        while q.qsize() > 0:
            tmp_ret = []
            tmp_list = []
            for tmp in q.get():
                tmp_ret.append(tmp.val)
                if tmp.left:
                    tmp_list.append(tmp.left)
                if tmp.right:
                    tmp_list.append(tmp.right)
            ret.append(tmp_ret)
            if tmp_list:
                q.put(tmp_list)
        return ret


def test():
    assert Solution().levelOrder(build_tree_node([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert Solution().levelOrder(build_tree_node([])) == []
    assert Solution().level_order(build_tree_node([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]


if __name__ == 'main':
    test()
