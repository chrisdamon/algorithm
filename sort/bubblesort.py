#!/usr/bin/python3
# -*- coding: utf-8 -*-


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


# def bubbleSortWrapper(array):
#     for i in range(len(array)):
#         flag = 1
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#                 flag = 0
#             if flag:
#                 break
#     return array

if __name__ == '__main__':
    array = [2, 12, 45, 53, 44]
    # arrayWrapper = [11, 32, 24, 58, 47, 92, 88]
    # print(bubbleSort(array))
    # print(bubbleSortWrapper(arrayWrapper))