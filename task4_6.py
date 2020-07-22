from itertools import count, cycle


def my_count(start, finish, step):
    start, finish, step = int(start), int(finish), int(step)
    result = []

    for i in count(start, step):
        if i > finish:
            return result
        else:
            result.append(i)


print(my_count(3, 10, 1))


def my_cycle(my_list, finish):
    result = []
    n = 1
    for i in cycle(my_list):
        if n > finish:
            return result
        else:
            result.append(i)
            n += 1


print(my_cycle([1, "lol", None, 4.4546, -5], 10))
