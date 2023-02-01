some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# list.count checks for the number of times an item occurs in the list
# if its count is greater than one we add it to the list
# We use the built in set method to create a set that doesn't allow duplicate items
# then we convert the set back to a list
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)
