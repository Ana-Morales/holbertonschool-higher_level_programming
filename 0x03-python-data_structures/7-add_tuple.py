#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(len(tuple_a) + 1):
        if len(tuple_a) == 0:
            ta = 0, 0,
        elif len(tuple_a) == 1:
            ta = tuple_a + (0,)
        else:
            ta = tuple_a
        break
    for i in range(len(tuple_b) + 1):
        if len(tuple_b) == 0:
            tb = 0, 0,
        elif len(tuple_b) == 1:
            tb = tuple_b + (0,)
        else:
            tb = tuple_b
        break
    return (ta[0] + tb[0], ta[1] + tb[1])
