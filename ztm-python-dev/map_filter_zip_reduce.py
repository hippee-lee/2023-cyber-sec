from functools import reduce

# map, filter, reduce, zip

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def cap(word):
    return word.capitalize()


# Solution #1
print(list(map(cap, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

zipped_lists = list(zip(my_strings, my_numbers))


def sort_by_num(item1, item2):
    return item2[1] > item1[1]

    # Solution #2
sorted = zipped_lists.sort(key=lambda a: a[1])

print(zipped_lists)

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over50(item):
    return item > 50


print(list(filter(over50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def sum(x, y):
    return x + y


print(reduce(sum, scores) + reduce(sum, my_numbers))
