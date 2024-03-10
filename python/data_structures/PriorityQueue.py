import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __len__(self):
        return len(self._queue)
    
    def __str__(self) -> str:
        return str([item for _, _, item in self._queue])