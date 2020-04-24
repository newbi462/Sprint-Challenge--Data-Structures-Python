import time
# Student should be able to construct a binary search tree class
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# O(n^2) due to loop in loop +/- delta in Nss
"""
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""
# runtime: 5.88943338394165 seconds

use_tree = BinarySearchTree('not_a_name')

# add names to tree
for name_1 in names_1:
    use_tree.insert(name_1)

# are names 2 in tree
for name_2 in names_2:
    if use_tree.contains(name_2): #in practice may or may not be log n but should help
        duplicates.append(name_2) # matches would be duplicates
# runtime: 0.08811831474304199 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
