from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #pass
        if self.storage.length == self.capacity:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
        else:
            self.storage.add_to_head(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_node = self.storage.tail
        while list_node is not self.storage.head:
            list_buffer_contents.append(list_node.value)
            list_node = list_node.prev
            print(list_buffer_contents)

        list_buffer_contents.append(self.storage.tail.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
