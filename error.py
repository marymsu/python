#handling errors in python
try:
    age = int(input(f" Age:"))
    print(age)
except ValueError:
    print('Invalid value')


