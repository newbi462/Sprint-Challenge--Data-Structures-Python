class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        #pass
        # if no list return none your done


        if self.head == None:
            return None
        else:
            node_on = self.head
            next_node = self.head.get_next()
            last_node = None
            def recursion(node_on, next_node, last_node):
                print(node_on.value)
                print(node_on)
                print(next_node)
                print(last_node)
                print("-end of-")
                if next_node is not None:
                    node_on.set_next(last_node)
                    recursion(next_node, next_node.get_next(), node_on)
                else:
                    node_on.set_next(last_node)
                    self.head = node_on


        recursion(self.head, self.head.get_next(), None)

        # if list loop over util end

        #store pointers
        #repoint nodes
