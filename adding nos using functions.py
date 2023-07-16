#using a predefined function add, to find total of existing numbers 


def add(*numbers):
    total = 0
    for num in numbers:
        total = total+ num
    return total
print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))

#expected output:
5
10
17
26