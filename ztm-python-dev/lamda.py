# Square the list
my_list = [5, 4, 3]
print(list(map(lambda item: item * item, my_list)))

# List sorting
# List of tuples
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# Sort the list based on the second item in the tuple
# sorted = zipped_lists.sort(key=lambda a: a[1])
# Interesting - this class method sorts and modifies the list in place.
a.sort(key=lambda a: a[1])
print(a)
