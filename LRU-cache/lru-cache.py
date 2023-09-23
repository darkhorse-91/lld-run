"""
Caching -> Queries as key and results as Values
Assumptions -
    Inputs are valid.
    No memory overload

Methods needed in our LL interface
    move_to_head()
    add_to_head()
    del_from_tail()
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_head(self, node):
        pass

    def add_to_head(self, node):
        pass

    def del_from_tail(self):
        pass


class Cache:

    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.size = 0
        self.lookup = {}
        self.linkedlist = Linkedlist()

    def get_cache(self, query):
        node = self.lookup.get(query)
        if node is None:
            return None
        self.linkedlist.move_to_head(node)
        return node.val

    def set_cache(self, query, value):
        node = self.lookup.get(query)

        if node is not None:
            node.val = value
            self.linkedlist.move_to_head(node)
        else:
            if self.size == self.MAX_SIZE:
                self.lookup.pop(query, None)
                self.linkedlist.del_from_tail()
            else:
                self.size += 1
            new_node = Node(value)
            self.linkedlist.add_to_head(new_node)
            self.lookup[query] = new_node
