class Node:
    """Node class for the linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HachMap:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.buckets = [None] * self.capacity  # Each bucket will be a linked list

    def hash(self, key):
        """Hash function to calculate the bucket index."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash(key)

        # If the bucket is empty, create a new node
        if self.buckets[index] is None:
            self.buckets[index] = Node(key, value)
        else:
            # Traverse the linked list to find if the key exists
            current = self.buckets[index]
            while current:
                if current.key == key:  # Key exists, update value
                    current.value = value
                    return
                if current.next is None:  # Reached the end, insert new node
                    break
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)

        # Traverse the linked list to find the key
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None  # Key not found

    def remove(self, key):
        index = self.hash(key)

        # Traverse the linked list to find and remove the key
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:  # Remove the head node
                    self.buckets[index] = current.next
                else:  # Remove a node in the middle or end
                    prev.next = current.next
                return
            prev = current
            current = current.next

        raise KeyError("Key not found")

    def show(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}:", end=" ")
            current = bucket
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")


# Example Usage
example = HachMap()
example.insert("apple", 100)
example.insert("banana", 200)
example.insert("cherry", 300)
example.insert("apple", 150)  # Updates the value for 'apple'

example.show()

print("Get 'apple':", example.get("apple"))  # 150
example.remove("apple")
example.show()
