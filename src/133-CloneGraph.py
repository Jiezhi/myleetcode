#!/usr/bin/env python
"""
CREATED AT: 2022/2/23
Des:

https://leetcode.com/problems/clone-graph/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 11 min
"""
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Runtime: 91 ms, faster than 5.31%
        Memory Usage: 14.4 MB, less than 91.72%

        The number of nodes in the graph is in the range [0, 100].
        1 <= Node.val <= 100
        Node.val is unique for each node.
        There are no repeated edges and no self-loops in the graph.
        The Graph is connected and all nodes can be visited starting from the given node.
        """
        if not node:
            return None
        new_node = Node(node.val, [])
        visited = set()
        node_dict = dict()
        node_dict[node.val] = new_node
        dq = collections.deque([node])
        while dq:
            tmp_node = dq.popleft()
            visited.add(tmp_node.val)
            new_neighbor = []
            for neighbor in tmp_node.neighbors:
                if neighbor.val not in visited:
                    dq.append(neighbor)
                if neighbor.val not in node_dict:
                    node_dict[neighbor.val] = Node(neighbor.val, [])
                new_neighbor.append(node_dict[neighbor.val])
            node_dict[tmp_node.val].neighbors = new_neighbor

        return new_node


def test():
    # No tests
    pass


if __name__ == '__main__':
    test()
