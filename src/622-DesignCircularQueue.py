#!/usr/bin/env python
"""
Created on 2019/11/20

Des:
https://leetcode.com/problems/design-circular-queue/

"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._max_index = k - 1
        self._queue = [0] * k
        self._head = 0
        self._tail = -1
        self._size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self._tail == self._max_index:
            self._tail = 0
        else:
            self._tail += 1
        self._queue[self._tail] = value
        self._size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self._head == self._max_index:
            self._head = 0
        else:
            self._head += 1
        self._size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self._queue[self._head] if self._size > 0 else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self._queue[self._tail] if self._size > 0 else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._size == self._max_index + 1


def test():
    circularQueue = MyCircularQueue(3)
    assert circularQueue.enQueue(1)
    assert circularQueue.enQueue(2)
    assert circularQueue.enQueue(3)
    assert not circularQueue.enQueue(4)
    assert circularQueue.Rear() == 3
    assert circularQueue.isFull()
    assert circularQueue.deQueue()
    assert circularQueue.enQueue(4)
    assert circularQueue.Rear() == 4

    circularQueue = MyCircularQueue(6)
    assert circularQueue.enQueue(6)
    assert circularQueue.Rear() == 6
    assert circularQueue.Rear() == 6
    assert circularQueue.deQueue()
    assert circularQueue.enQueue(5)
    assert circularQueue.Rear() == 5
    assert circularQueue.deQueue()
    assert circularQueue.Front() == -1

    circularQueue = MyCircularQueue(3)
    assert circularQueue.enQueue(2)
    assert circularQueue.Rear() == 2
    assert circularQueue.Front() == 2


if __name__ == '__main__':
    test()
