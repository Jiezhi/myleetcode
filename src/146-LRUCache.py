#!/usr/bin/env python
"""
CREATED AT: 2021/12/29
Des:

https://leetcode.com/problems/lru-cache/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Note: See collections.OrderedDict

Time Spent:  min
"""


class DoubleLinkedNode:
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class LRUCache:
    """
    Runtime: 982 ms, faster than 26.01%
    Memory Usage: 77.3 MB, less than 5.61%
    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls will be made to get and put.
    """

    def __init__(self, capacity: int):
        # dict key is tuple (value, node)
        self.cache_dict = {}
        self.capacity = capacity
        self.head = DoubleLinkedNode(-1)
        self.tail = self.head

    def update_list(self, node):
        if node.next and node.pre:
            # node not at the tail of list
            node.pre.next = node.next
            node.next.pre = node.pre
            node.next = None
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        else:
            node = self.cache_dict[key][1]
            self.update_list(node)
            return self.cache_dict[key][0]

    def put(self, key: int, value: int) -> None:
        # key in cache, update value and position in list
        if key in self.cache_dict:
            node: DoubleLinkedNode = self.cache_dict[key][1]
            node.val = key
            self.update_list(node)
            self.cache_dict[key] = (value, node)
        elif len(self.cache_dict) < self.capacity:
            node = DoubleLinkedNode(key)
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
            self.cache_dict[key] = (value, node)
        else:
            # need to remove one node
            self.head = self.head.next
            self.head.pre = None
            self.cache_dict.pop(self.head.val)
            self.put(key, value)


def test():
    capacity = 2
    obj = LRUCache(capacity)
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    obj.put(3, 3)
    assert obj.get(2) == -1
    obj.put(4, 4)
    assert obj.get(1) == -1
    assert obj.get(3) == 3
    assert obj.get(4) == 4

    obj = LRUCache(capacity=capacity)
    obj.put(1, 0)
    obj.put(2, 2)
    assert obj.get(1) == 0
    obj.put(3, 3)
    assert obj.get(2) == -1
    obj.put(4, 4)
    assert obj.get(3) == 3
    assert obj.get(4) == 4


if __name__ == '__main__':
    test()
