#import sys
#sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #pass
        # self.left and/or self.right need to be valid nodes
        # for us to call `insert` on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTree(value)
        else: # otherwise, value >= self.value
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #pass
        if self.value == target:
            return True
        else:
            if self.value < target:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
            else:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        #pass
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass
        cb(self.value)
        if self.right: # get the right
            self.right.for_each(cb)

        if self.left: #get the left
            self.left.for_each(cb)

    def depth_first_iterative_for_each(self, cb):
        stack = []
        # add the root of the tree to the stack
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_iterative_for_each(self, cb):
        # depth-first : stack
        # breadth-first : queue
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #pass
        if self.left: # get the right
            self.left.in_order_print(node)
        #print(f"print {self.value}") print will only show in an f stament why?
        print(self.value)

        if self.right: # get the right
            self.right.in_order_print(node)




    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #pass
        hold = Queue()
        hold.enqueue(node)
        while hold.len() > 0:
            cycle = hold.dequeue()
            if cycle.left is not None:
                hold.enqueue(cycle.left)
            if cycle.right is not None:
                hold.enqueue(cycle.right)
            print(cycle.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #pass
        hold = Stack()
        hold.push(node)
        while hold.len() > 0:
            cycle = hold.pop()
            if cycle.left is not None:
                hold.push(cycle.left)
            if cycle.right is not None:
                hold.push(cycle.right)
            print(cycle.value)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


test = BinarySearchTree(4)
test.insert(5)
test.insert(3)
test.insert(20)
test.insert(6)

print(test.contains(10))
print(test.get_max())
