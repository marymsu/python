#Question One creating a tuple

week = ("Monday", "Tuesday","Wednesday", "Thursday","Friday", "Saturday", "Sunday",)

print(week)

#Question Two creating a set

fruits = set(['apple', 'mango','orange'])

print(fruits)

#Question Three difference in a set

fruits = set(['apple', 'mango','orange'])
new_fruits = {'cherry', 'peach', 'apple', 'mango'}
print(new_fruits.difference(fruits))


#Question Three Intersection in a set
fruits = set(['apple', 'mango','orange'])
new_fruits = {'cherry', 'peach', 'apple', 'mango'}
print(new_fruits.intersection(fruits))
