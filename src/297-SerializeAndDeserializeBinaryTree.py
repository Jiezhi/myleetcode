#!/usr/bin/env python
"""
CREATED AT: 2022/4/27
Des:
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See:  https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/883704/JavaPython-2-solutions:-DFS-BFS-O(N)-Clean-and-Concise/1234193

"""

import collections

from tree_node import TreeNode


class Codec:
    """
    Runtime: 229 ms, faster than 67.12%
    Memory Usage: 20.2 MB, less than 83.74%

    The number of nodes in the tree is in the range [0, 10^4].
    -1000 <= Node.val <= 1000
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return f'{str(root.val)},{self.serialize(root.left)},{self.serialize(root.right)}' if root else '#'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(dq):
            if not dq:
                return None
            node = dq.popleft()
            if node == '#':
                return None
            root = TreeNode(int(node))
            root.left = dfs(dq)
            root.right = dfs(dq)
            return root

        return dfs(collections.deque(data.split(',')))


def test():
    null = None
    data = Codec().serialize(TreeNode.from_list([1, 2, 3, null, null, 4, 5]))
    assert Codec().deserialize(data) == TreeNode.from_list([1, 2, 3, null, null, 4, 5])


if __name__ == '__main__':
    test()
