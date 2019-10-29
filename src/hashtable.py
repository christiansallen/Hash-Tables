# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        # Start from an arbitrary large prime
        hash_value = 5381
    # Bit-shift and sum value for each character
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        char_sum = 0
        for c in f"{self._hash(key)}":
            char_sum += ord(c)
        return char_sum % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is None:
            node = LinkedPair(key, value)
            self.storage[index] = node
            return
        else:
            if node.key == key:
                node.value = value
                return
            while node.next is not None:
                node = node.next
                if node.key == key:
                    node.value = value
                    return
            node.next = LinkedPair(key, value)
            return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        node = self.storage[index]
        if node.key == key:
            if node.next is not None:
                next_node = node.next
                node = next_node
            else:
                node = None
        else:
            prev_node = None
            current_node = node
            next_node = node.next
            while next_node is not None:
                prev_node = node
                current_node = next_node
                next_node = current_node.next
                if current_node.key == key:
                    prev_node.next = next_node
                    return
        print("Key is not found")
        return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is not None:
            if node.key == key:
                return node.value
            else:
                while node.next is not None:
                    node = node.next
                    if node.key == key:
                        return node.value
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = [None] * self.capacity
        # Copy old items to new storage
        for i in range(0, len(self.storage)):
            new_storage[i] = self.storage[i]
        # Point storage to the new storage
        self.storage = [None]*self.capacity*2
        self.capacity *= 2
        for i in new_storage:
            if i is not None:
                node = i
                while node.next is not None:
                    self.insert(node.key, node.value)
                    node = node.next
                self.insert(node.key, node.value)


if __name__ == "__main__":
    ht = HashTable(30)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
