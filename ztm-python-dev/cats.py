# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat0 = Cat('barn-cat', 99)
cat1 = Cat('ash-the-gray', 4)
cat2 = Cat('peaches', 5)
cat3 = Cat('coco', 6)
cat4 = Cat('lark', 1009)


# 2 Create a function that finds the oldest cat
def oldest_cat(cats):
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat
    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
old_cat = oldest_cat([cat0, cat1, cat2, cat3, cat4])
print(f'the olodest cat is {old_cat.age} years old')
