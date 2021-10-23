#!/usr/bin/env python
"""
Created on 20210719

Des:
https://leetcode.com/problems/design-linked-list/

"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        else:
            i = 0
            tmp_node: Node = self.first
            while i < index:
                tmp_node = tmp_node.next
                i += 1
            return tmp_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp_node: Node = Node(val)
        tmp_node.next = self.first
        self.first = tmp_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # i = 1
        # tmp_node = self.first
        # while i < self.length:
        #     tmp_node = tmp_node.next
        # tmp_node.next = Node(val)
        # # self.first = tmp_node
        # self.length += 1

        self.addAtIndex(index=self.length, val=val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        i = 1
        tmp_node = self.first
        while i < index:
            tmp_node = tmp_node.next
            i += 1
        insert_node = Node(val)
        insert_node.next = tmp_node.next
        tmp_node.next = insert_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        if index == 0:
            self.first = self.first.next
            return
        i = 1
        tmp_node = self.first
        while i < index:
            tmp_node = tmp_node.next
            i += 1
        tmp_node.next = tmp_node.next.next
        self.length -= 1

    def debug_print(self):
        val_list = []
        tmp_node = self.first
        while tmp_node:
            val_list.append(tmp_node.val)
            tmp_node = tmp_node.next
        print(val_list)
        return val_list


def test():
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    assert obj.debug_print() == []
    # param_1 = obj.get(0)
    obj.addAtHead(1)
    assert obj.debug_print() == [1]
    obj.addAtTail(0)
    assert obj.debug_print() == [1, 0]
    obj.addAtIndex(1, 10)
    assert obj.debug_print() == [1, 10, 0]
    assert obj.get(2) == 0
    assert obj.get(3) == -1

    assert obj.get(0) == 1
    assert obj.get(1) == 10
    assert obj.get(2) == 0

    obj.deleteAtIndex(1)
    assert obj.debug_print() == [1, 0]

    obj.deleteAtIndex(1)
    assert obj.debug_print() == [1]
    obj.deleteAtIndex(1)
    assert obj.debug_print() == [1]

    # ["MyLinkedList","addAtHead","deleteAtIndex"]
    # [[],[1],[0]]

    obj = MyLinkedList()
    obj.addAtHead(1)
    assert obj.debug_print() == [1]
    obj.deleteAtIndex(0)
    assert obj.debug_print() == []

    # ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
    # [[],[0,10],[0,20],[1,30],[0]]
    obj = MyLinkedList()
    obj.addAtIndex(0, 10)
    assert obj.debug_print() == [10]
    obj.addAtIndex(0, 20)
    assert obj.debug_print() == [20, 10]
    obj.addAtIndex(1, 30)
    assert obj.debug_print() == [20, 30, 10]
    assert obj.get(0) == 20

    # ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead",
    # "addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
    # [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]


if __name__ == '__main__':
    test()
