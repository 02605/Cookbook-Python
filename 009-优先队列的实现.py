import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # self._index的目的是确保堆的特征
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('ads'), 4)
q.push(Item('dsf'), 5)
q.push(Item('daw'), 1)
# foo与daw的优先级相同，会根据插入顺序_index来弹出先插入的foo
# (1, 0, Item('foo')) < (1, 3, Item('daw'))
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

