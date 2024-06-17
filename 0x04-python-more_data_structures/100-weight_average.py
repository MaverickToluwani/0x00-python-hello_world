#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_SW = 0
    total_weight = 0
    for row in range(len(my_list)):
        for col in range(len(my_list[0]) - 1):
            sum_SW = sum_SW + (my_list[row][col] * my_list[row][col+1])
            total_weight = total_weight + my_list[row][col+1]
    weight_avg = sum_SW / total_weight
    return weight_avg
