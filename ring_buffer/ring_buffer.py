from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None # use this as a counter do to nither FIFO or LIFO
        self.storage = DoublyLinkedList()

    def append(self, item):
        #pass
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            if self.storage.length < self.capacity:
                self.storage.add_to_tail(item)
                self.storage.tail.next = self.storage.head
            else:
                self.current.value = item
                self.current = self.current.next



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_node = self.storage.head
        while list_node is not self.storage.tail:
            list_buffer_contents.append(list_node.value)
            list_node = list_node.next
            print(list_buffer_contents)
            # reverse head and tail to use counter

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
