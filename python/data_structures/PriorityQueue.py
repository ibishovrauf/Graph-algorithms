import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self) -> tuple:
        return heapq.heappop(self._queue)

    def __len__(self):
        return len(self._queue)
    
    def __str__(self) -> str:
        return str([(dist, str(item)) for dist, _, item in self._queue])
    
    def __bool__(self) -> bool:
        return len(self._queue) != 0