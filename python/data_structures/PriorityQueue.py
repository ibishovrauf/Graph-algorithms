import heapq

class PriorityQueue:
    def __init__(self) -> None:
        """
        Initializes an empty priority queue.
        """
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        Pushes an item onto the priority queue with the given priority.

        Args:
            item: The item to push onto the queue.
            priority: The priority of the item.
        """
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self) -> tuple:
        """
        Pops and returns the item with the lowest priority from the priority queue.

        Returns:
            tuple: A tuple containing the priority, index, and item popped from the queue.
        """
        return heapq.heappop(self._queue)

    def __len__(self):
        """
        Returns the number of items in the priority queue.
        """
        return len(self._queue)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the priority queue.
        """
        return str([(dist, str(item)) for dist, _, item in self._queue])
    
    def __bool__(self) -> bool:
        """
        Checks if the priority queue is non-empty.

        Returns:
            bool: True if the priority queue is non-empty, False otherwise.
        """
        return len(self._queue) != 0
