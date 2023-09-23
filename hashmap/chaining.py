"""
We need to implement hashmap

For Simplicity 
    Collision -> Chaining
    Key -> int
    Memory -> managed
    Input ->  Validated
    Load Factors -> NO
"""


class Item:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class CustomHash:

    def __init__(self, size: int) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def search(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError("Key Not Found")

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index in range(len(self.table[hash_index])):
            if self.table[hash_index][index].key == key:
                del self.table[hash_index][index]
                return
        raise KeyError("Key Not Found")
