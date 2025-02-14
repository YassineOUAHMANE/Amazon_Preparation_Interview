class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __parent(self, i):
        return (i - 1) // 2

    def __left_child(self, i):
        return 2 * i + 1

    def __right_child(self, i):
        return 2 * i + 1 + 1

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __heapify_up(self, i):
        while i > 0 and self.heap[self.__parent(i)] > self.heap[i]:
            self.__swap(i, self.__parent(i))
            i = self.__parent(i)

    def __heapify_down(self, i):
        smallest = i
        left = self.__left_child(i)
        right = self.__right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.__swap(i, smallest)
            self.__heapify_down(smallest)

    def insert(self, element):
        self.heap.append(element)
        self.__heapify_up(len(self.heap) - 1)

    def remove_min(self):
        if len(self.heap) == 0:
            raise IndexError("Priority Queue is empty")

        min_element = self.heap[0]
        # Move the last element to the root and heapify down
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__heapify_down(0)

        return min_element

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Priority Queue is empty")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

# Example usage
pq = PriorityQueue()
pq.insert(5)
pq.insert(3)
pq.insert(8)
pq.insert(1)

print(f"Min Element: {pq.peek()}")  # Output: Min Element: 1

print(f"Removed Min: {pq.remove_min()}")  # Output: Removed Min: 1
print(f"Min Element: {pq.peek()}")  # Output: Min Element: 3

print(f"Queue Size: {pq.size()}")  # Output: Queue Size: 3
