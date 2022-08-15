#!/usr/bin/env python3
"""
CREATED AT: 2022-08-15

URL: https://leetcode.com/problems/design-circular-deque/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 641-DesignCircularDeque

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class ListNode:
    def __init__(self, x=None, nxt=None):
        self.val = x
        self.next = nxt


class MyCircularDeque:
    """
    TODO: Use Double Linked List
    Runtime: 124 ms, faster than 32.88%
    Memory Usage: 14.6 MB, less than 60.45%

    1 <= k <= 1000
    0 <= value <= 1000
    At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
    """

    def __init__(self, k: int):
        self.capcity = k
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size >= self.capcity:
            return False
        tmp = ListNode(value, self.head.next)
        self.head.next = tmp
        self.size += 1

        if self.size == 1:
            self.tail = self.head.next
        return True

    def insertLast(self, value: int) -> bool:
        if self.size >= self.capcity:
            return False
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.head.next = self.head.next.next
        self.size -= 1
        if self.size == 0:
            self.tail = self.head
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        # O(n), if want O(1) use Double Linked List
        self.tail = self.head
        i = 0
        while i < self.size - 1:
            self.tail = self.tail.next
            i += 1
        self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.size == 0 else self.head.next.val

    def getRear(self) -> int:
        return -1 if self.size == 0 else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capcity


def test():
    mcd = MyCircularDeque(5)
    assert mcd.insertFront(7)
    assert mcd.deleteLast()
    assert mcd.insertFront(7)
    assert mcd.insertLast(0)
    assert mcd.getFront() == 7
    assert mcd.insertLast(3)
    assert mcd.insertFront(9)
    assert mcd.deleteLast()
    assert mcd.getRear() == 0

    mcd = MyCircularDeque(3)
    assert mcd.insertLast(1)
    assert mcd.insertLast(2)
    assert mcd.insertFront(3)
    assert not mcd.insertFront(4)
    assert mcd.getRear() == 2
    assert mcd.isFull()
    assert mcd.deleteLast()
    assert mcd.getRear() == 1
    assert mcd.insertFront(4)
    assert mcd.getFront() == 4


if __name__ == '__main__':
    test()
