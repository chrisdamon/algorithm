#!/usr/bin/python3
# -*- coding: utf-8 -*-


def binarySearch(array, item):
    '''
    在一个有序的序列中查找值，返回该值在序列中的下标
    :param array: 有序序列
    :param item: 要查找的值
    :return: 下标
    '''
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        if item == array[middle]:
            return middle
        if item > array[middle]:
            low = middle + 1
        if item < array[middle]:
            high = middle - 1
    return None


if __name__ == '__main__':
    array = [1, 2, 4, 8, 16, 32, 64]
    item = 8
    print(binarySearch(array, item))