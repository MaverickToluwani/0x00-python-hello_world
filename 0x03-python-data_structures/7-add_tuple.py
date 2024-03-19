#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) < 1:
            firstAdd = 0 + tuple_b[0]
            secondAdd = 0 + tuple_b[1]
            return (firstAdd, secondAdd)
        else:
            firstAdd = tuple_a[0] + tuple_b[0]
            secondAdd = 0 + tuple_b[1]
            return (firstAdd, secondAdd)
    elif len(tuple_b) < 2:
        if len(tuple_b) < 1 or len(tuple_b) == 0:
            firstAdd = 0 + tuple_a[0]
            secondAdd = 0 + tuple_a[1]
            return (firstAdd, secondAdd)
        else:
            firstAdd = tuple_a[0] + tuple_b[0]
            secondAdd = 0 + tuple_a[1]
            return (firstAdd, secondAdd)
    elif len(tuple_a) < 2 and len(tuple_b) < 2:
        if len(tuple_a < 1) and len(tuple_a < 1):
            firstAdd = 0 + 0
            secondAdd = 0 + 0
            return (firstAdd, secondAdd)
        else:
            firstAdd = tuple_a[0] + tuple_b[0]
            secondAdd = 0 + 0
            return (firstAdd, secondAdd)
    elif len(tuple_a) > 1 or len(tuple_b) > 1:
        firstAdd = tuple_a[0] + tuple_b[0]
        secondAdd = tuple_a[1] + tuple_b[1]
        return (firstAdd, secondAdd)
